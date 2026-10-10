package main

import "fmt"

func main() {
	var conferenceName = "GO CONFERENCE"
	const conferenceTickets = 50

	fmt.Println("welcome to", conferenceName, "booking application")
	fmt.Println("Get your tickets here to attend")

	conferenceTickets = 30
	fmt.Println(conferenceTickets)

}
