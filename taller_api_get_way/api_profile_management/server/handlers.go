package server

import (
	"context"
	"encoding/json"
	"fmt"
	"net/http"
)

func index(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodGet {
		w.WriteHeader(http.StatusMethodNotAllowed)
		fmt.Fprint(w, "Method not allowed")
		return
	}

	fmt.Fprint(w, "Hello there ", "visitor")
}

func getCountries(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

}

func getProfile(w http.ResponseWriter, r *http.Request) {

}

// w lo utilizamos para metodos get
// r para metodos post
func update_profile(w http.ResponseWriter, r *http.Request, ctx context.Context) {
	profile := &Profile{}
	// decodifica el json de la cabecera del msj, aca ya tenemos los datos
	err := json.NewDecoder(r.Body).Decode(profile)
	// si hay un error se muestra el mensaje
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		fmt.Fprintf(w, "%v", err)
		return
	}

	// q := "SELECT * FROM profiles"

	// // Realizar una consulta
	// rows, err := db.DB.QueryContext(ctx, q)
	// if err != nil {
	// 	panic(err)
	// }
	// defer rows.Close()

	// for rows.Next() {
	// 	var id int
	// 	var name string
	// 	if err := rows.Scan(&id, &name); err != nil {
	// 		panic(err)
	// 	}
	// 	fmt.Println(id, name)
	// }

	// countries = append(countries, country)
	// fmt.Fprint(w, "country was addedd")
}
