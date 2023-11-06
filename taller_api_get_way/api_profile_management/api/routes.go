package api

import "github.com/gorilla/mux"

func (a *API) RegisterRoutes(r *mux.Router) {

	r.HandleFunc("/", a.index)
	r.HandleFunc("/profiles/:{email}", a.getProfile).Methods("GET")
	//r.HandleFunc("/profiles/me", a.getPersonalProfile).Methods("GET")
	r.HandleFunc("/profiles/:{email}", a.updateProfile).Methods("PUT")
}
