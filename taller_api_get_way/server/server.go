package server

import (
	"net/http"

	"github.com/gorilla/mux"
)

// var UserAutenticado = "cristiano_r@email.com"
var UserAutenticado = "sin_autenticar"

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

type Server struct {
	server *http.Server
}

func New(addr string, r *mux.Router) *http.Server {
	return &http.Server{
		Addr:    addr,
		Handler: r,
	}
}
