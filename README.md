# microbit-door-sensor

The system is divided into more parts:
  - The door sensor (connected to the receiver by radio)
  - The receiver (connected to the PC via serial)
  - The PC with the WebSocket server and the node site.

In the flask.py file, you can view the first prototype with a single web server that gets door status and displays that when the page is loaded.

Then I made a website that updates live when the door is open or closed with a WebSockets server.

To run it you need to install pyserial, websockets, and flask.
To run the website, go to the site directory and run `npm install` to install dependencies and `npm run dev -- --open` for running the website. 

<details>
  <summary>Microbit door Sensor</summary>
  
  ![20231008_133104](https://github.com/Fytecas/microbit-door-sensor/assets/98255583/537a8eff-50b5-4a32-9586-f842a2729dcb)

</details>

<details>
  <summary>Door Sensor</summary>
  
  ![20231008_133152](https://github.com/Fytecas/microbit-door-sensor/assets/98255583/6e585571-977a-45d6-bfa9-e644d7ed819e)

  
</details>

<details>
  <summary>Receiver (connected to the pc)</summary>
  
  ![20231008_122354](https://github.com/Fytecas/microbit-door-sensor/assets/98255583/11093cea-84ee-45b5-bf39-55ab4c188dfd)
  
</details>

<details>
  <summary>Website screenshot</summary>
  
  ![Website interface](https://github.com/Fytecas/microbit-door-sensor/assets/98255583/09e8f668-1b9c-4cac-9b6d-b70db09c55e2)

</details>
