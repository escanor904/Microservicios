package api

import (
	"apigetWay/api_gestion/data"
	"encoding/json"
	"fmt"
	"io"
	"strings"

	"net/http"

	"github.com/dgrijalva/jwt-go"
	"github.com/gorilla/mux"
)

// la variable con "" quere decir que no hay ususario logeado
// var usuarioEnSesion = ""
var usuarioEnSesion = "cristiano_r@email.com"
var tokenString = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5OTIzOTg1MSwianRpIjoiNGNhOWM4MDQtYmI2Yi00YTExLWJiYzQtODhhMDkyZGU0NTcwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImNyaXN0aWFub19yQGVtYWlsLmNvbSIsIm5iZiI6MTY5OTIzOTg1MSwiZXhwIjoxNjk5MjQwNzUxfQ.VQb_LCipFwWwD6jTrjn6shkhkUswmM_WAFpOtFU_C2Y"

const SECRET_KEY = "mypass"

type API struct {
}
type Profile struct {
	Email             string
	Username          string
	PersonalPage      string
	Correspondence    string
	Biography         string
	Organization      string
	Country           string
	LinkedInURL       string
	PublicInformation bool
}

func (a *API) index(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodGet {
		w.WriteHeader(http.StatusMethodNotAllowed)
		fmt.Fprint(w, "Method not allowed")
		return
	}

	fmt.Fprint(w, "Hello there ", "visitor")
}

func (a *API) updateProfile(w http.ResponseWriter, r *http.Request) {
	// creamos la estructura donde insertaremos el json de entrada
	w.Header().Set("Content-Type", "application/json")
	vars := mux.Vars(r)
	emailUser := vars["email"]

	if usuarioEnSesion != "" {
		if usuarioEnSesion == emailUser {
			if usuarioEnSesion != "" {
				type act struct {
					Username          string
					PersonalPage      string
					Correspondence    string
					Biography         string
					Organization      string
					Country           string
					LinkedInURL       string
					PublicInformation bool
				}

				var dataJson act
				//leemos el json
				reqBody, err := io.ReadAll(r.Body)
				if err != nil {
					return
				}

				json.Unmarshal(reqBody, &dataJson)

				//se obtiene la instancia a la base de datos
				q := fmt.Sprintf("UPDATE profiles set username = '%s', pagina_personal = '%s', correspondencia = '%s', biografia = '%s', organizacion = '%s', pais = '%s', linkedln_url = '%s', informacion_publica= '%t'  WHERE  email = '%s'", dataJson.Username, dataJson.PersonalPage, dataJson.Correspondence, dataJson.Biography, dataJson.Organization, dataJson.Country, dataJson.LinkedInURL, dataJson.PublicInformation, usuarioEnSesion)
				db := data.GetConection()
				defer db.Close()

				//implementamos la consulta para actualizar los datos
				rows, err := db.Query(q)
				if err != nil {
					panic(err)
				}
				defer rows.Close()

				message := map[string]string{
					"Info": "El usuario: " + usuarioEnSesion + " Fue actualizado con exito"}
				json.NewEncoder(w).Encode(message)

			} else {
				w.WriteHeader(http.StatusAccepted)
				message := map[string]string{
					"error": "Necesitas estar autenticado en el sistema para consultar tu perfil "}
				json.NewEncoder(w).Encode(message)
			}

		} else {
			w.WriteHeader(http.StatusBadRequest)
			message := map[string]string{"error": "El usuario al que se quiere actualizar es diferente al que esta en sesión: "}
			json.NewEncoder(w).Encode(message)
		}
	} else {
		w.WriteHeader(http.StatusBadRequest)
		message := map[string]string{"error": "Debe tener un usuario autenticado en el sistema para actualizar el perfil: "}
		json.NewEncoder(w).Encode(message)
	}

}

func (a *API) getProfile(w http.ResponseWriter, r *http.Request) {
	// Obtener el valor del encabezado 'Authorization'
	authHeader := r.Header.Get("Authorization")

	// Quitar el prefijo 'Bearer ' del encabezado 'Authorization'
	token := strings.TrimPrefix(authHeader, "Bearer ")

	if tokenIsValid(token) {
		//si el token es valido

		//obtenemos el usuario del token
		usuarioEnSesion = getEmail(token)

		w.Header().Set("Content-Type", "application/json")
		vars := mux.Vars(r)
		emailUser := vars["email"]

		profile := &Profile{}

		//se obtiene la instancia a la base de datos
		q := fmt.Sprintf("SELECT * FROM profiles WHERE email = '%s'", emailUser)
		db := data.GetConection()
		defer db.Close()

		//implementamos la consulta
		rows, err := db.Query(q)
		if err != nil {
			panic(err)
		}
		defer rows.Close()

		//Escanear los resultados
		for rows.Next() {
			err = rows.Scan(&profile.Email, &profile.Username, &profile.PersonalPage, &profile.Correspondence, &profile.Biography, &profile.Organization, &profile.Country, &profile.LinkedInURL, &profile.PublicInformation)
			if err != nil {
				panic(err)
			}
		}

		if profile.Email != "" {
			//si la consulta trae datos

			if profile.Email == usuarioEnSesion {
				//si el usuario que se va a consultar es el usuario logeado
				w.WriteHeader(http.StatusAccepted)
				json.NewEncoder(w).Encode(profile)

			} else {
				//si el usuario es diferente del que esta en sesión se verifica si el usuario a consultar
				// permite ver su información de contacto
				if profile.PublicInformation == true {
					//manda el json de respuesta a el usuario que tiene habilitada la información de contacto
					w.WriteHeader(http.StatusAccepted)
					json.NewEncoder(w).Encode(profile)
				} else {
					w.WriteHeader(http.StatusAccepted)
					message := map[string]string{
						"error": "En este momento, el perfil que estás buscando no dispone de información pública. "}
					json.NewEncoder(w).Encode(message)
				}
			}

		} else {
			w.WriteHeader(http.StatusBadRequest)
			message := map[string]string{"error": "No se encontraron resultados para el email: " + emailUser}
			json.NewEncoder(w).Encode(message)
		}
	} else {
		w.WriteHeader(http.StatusBadRequest)
		message := map[string]string{"error": "El token no cumplió con los protocolos de autenticidad"}
		json.NewEncoder(w).Encode(message)
	}

}

func getEmail(tokenStr string) string {

	claims := jwt.MapClaims{}
	jwt.ParseWithClaims(tokenStr, claims, func(token *jwt.Token) (interface{}, error) {
		return []byte(SECRET_KEY), nil
	})

	usuario := claims["sub"].(string)
	return usuario
}

func tokenIsValid(tokenStr string) bool {

	token, err := jwt.Parse(tokenStr, func(token *jwt.Token) (interface{}, error) {
		return []byte(SECRET_KEY), nil
	})

	if err != nil {
		return false
	}

	return token.Valid

}
