package server

import (
	"fmt"
	"net/http"
)

func initRoutes() {
	http.HandleFunc("/hola", index)
	//fmt.Sprintf("Los números son %d y %d", a, b)
	//"(/user/:{}"
	http.HandleFunc(fmt.Sprintf("/profiles/:{email}"), func(w http.ResponseWriter, r *http.Request) {

		switch r.Method {
		case http.MethodGet:
			//getProfile(w, r)

		default:
			w.WriteHeader(http.StatusMethodNotAllowed)
			fmt.Fprint(w, "Method not allowed")
			return
		}
	})

}
