package data

import (
	"database/sql"
	"fmt"
	"log"
	"os"

	_ "github.com/lib/pq"
)

// para exportar esta función desde otro paquete la letra debe empezar n mayuscula para que sea una función publica
func GetConection() *sql.DB {

	// Obtener los valores de las variables de entorno
	dbUser := os.Getenv("DB_USER")
	dbPassword := os.Getenv("POSTGRES_PASSWORD")
	dbName := os.Getenv("DB_NAME")
	dbHost := os.Getenv("DATABASE_HOST")
	dbPort := os.Getenv("DATABASE_PORT")

	// Construir la cadena de conexión dsn
	dsn := fmt.Sprintf("postgres://%s:%s@%s:%s/%s?sslmode=disable", dbUser, dbPassword, dbHost, dbPort, dbName)
	//dsn := "postgres://admin:admin_password@localhost:5433/profile_db?sslmode=disable"
	db, err := sql.Open("postgres", dsn)
	if err != nil {
		log.Fatalf("Error: Unable to connect to database: %v", err)
	}

	return db

}
