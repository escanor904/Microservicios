package data

import (
	"database/sql"
	"log"

	_ "github.com/lib/pq"
)

// para exportar esta función desde otro paquete la letra debe empezar n mayuscula para que sea una función publica
func GetConection() *sql.DB {
	dsn := "postgres://admin:admin_password@localhost:5433/profile_db?sslmode=disable"
	db, err := sql.Open("postgres", dsn)
	if err != nil {
		log.Fatalf("Error: Unable to connect to database: %v", err)
	}

	log.Printf("Connected to the database")

	return db

}
