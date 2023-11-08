package data

import (
	"context"
	"encoding/json"
	"fmt"
	"log"

	"github.com/segmentio/kafka-go"
)

type Registro struct {
	EventType string `json:"event_type"`
	Username  string `json:"username"`
	UserEmail string `json:"user_email"`
	Timestamp string `json:"timestamp"`
}

// el metodo tiene que comenzar por mayuscula para que sea publico
func EscucharEventos() {

	log.Printf("Consumer managment lisening")

	r := kafka.NewReader(kafka.ReaderConfig{
		Brokers:   []string{"localhost:9093"},
		Topic:     "managment-topic",
		Partition: 0,
		MinBytes:  10e3,
		MaxBytes:  10e6,
	})

	r.SetOffset(0)

	for {
		m, err := r.ReadMessage(context.Background())

		if err != nil {
			break
		}

		registro := Registro{}
		err = json.Unmarshal(m.Value, &registro)

		// insertar nuevos usuarios a la base de datos
		var count int
		db := GetConection()
		q := fmt.Sprintf("SELECT COUNT(*) FROM profiles WHERE email = '%s'", registro.UserEmail)
		err = db.QueryRow(q).Scan(&count)
		if err != nil {
			// Manejar el error de consulta
			log.Printf("Error en la consulta: %s", err)
			panic(err)
		}

		if count == 0 {
			fmt.Printf(registro.UserEmail)

			q = fmt.Sprintf("INSERT INTO profiles (email, username, pagina_personal, correspondencia, biografia, organizacion, pais, linkedln_url, informacion_publica) VALUES ('%s', '%s', '', '', '', '', '', '', %t)", registro.UserEmail, registro.Username, true)
			db = GetConection()
			results, err := db.Query(q)
			if err != nil {
				panic(err)
			}
			defer results.Close()
			fmt.Printf("se registro un nuevo usuario %d: %s = %s\n", m.Offset, string(m.Key), string(m.Value))
		}

	}

}
