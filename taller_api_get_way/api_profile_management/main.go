package main

import (
	"apigetWay/api_gestion/api"
	"apigetWay/api_gestion/data"
	"net/http"

	"github.com/gorilla/mux"
)

func main() {

	//enrutador
	go data.EscucharEventos()
	router := mux.NewRouter().StrictSlash(true)

	//create the API object
	a := &api.API{}

	//register the routes
	a.RegisterRoutes(router)

	srv := &http.Server{
		Addr:    ":8080",
		Handler: router,
	}

	err := srv.ListenAndServe()

	if err != nil {
		panic(err)
	}

}
