package api

import (
	"apigetWay/api_gestion/data"
	"encoding/json"
	"fmt"
	"io"

	"net/http"

	"github.com/gorilla/mux"
)

// la variable con "" quere decir que no hay ususario logeado
// var usuarioEnSesion = ""
var usuarioEnSesion = "cristiano_r@email.com"

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

func (a *API) getPersonalProfile(w http.ResponseWriter, r *http.Request) {

	w.Header().Set("Content-Type", "application/json")
	if usuarioEnSesion != "" {
		//se obtiene la instancia a la base de datos
		profile := &Profile{}
		q := fmt.Sprintf("SELECT * FROM profiles WHERE email = '%s'", usuarioEnSesion)
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

		w.WriteHeader(http.StatusAccepted)
		json.NewEncoder(w).Encode(profile)

	} else {
		w.WriteHeader(http.StatusAccepted)
		message := map[string]string{
			"error": "Necesitas estar autenticado en el sistema para consultar tu perfil "}
		json.NewEncoder(w).Encode(message)
	}

}

func (a *API) updateProfile(w http.ResponseWriter, r *http.Request) {
	// creamos la estructura donde insertaremos el json de entrada
	w.Header().Set("Content-Type", "application/json")
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

}

func (a *API) getProfile(w http.ResponseWriter, r *http.Request) {

	w.Header().Set("Content-Type", "application/json")
	vars := mux.Vars(r)
	emailUser := vars["email"]

	if r.Method != http.MethodGet {
		w.WriteHeader(http.StatusMethodNotAllowed)
		fmt.Fprint(w, "Method not allowed")
		return

	} else {

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

			if profile.PublicInformation == true {
				//manda el json de respuesta su el usuario tiene habilitada la información de contacto
				w.WriteHeader(http.StatusAccepted)
				json.NewEncoder(w).Encode(profile)
			} else {
				w.WriteHeader(http.StatusAccepted)
				message := map[string]string{
					"error": "En este momento, el perfil que estás buscando no dispone de información pública. "}
				json.NewEncoder(w).Encode(message)
			}

		} else {
			w.WriteHeader(http.StatusBadRequest)
			message := map[string]string{"error": "No se encontraron resultados para el email: " + emailUser}
			json.NewEncoder(w).Encode(message)
		}

	}

}
