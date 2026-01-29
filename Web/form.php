<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {

    $juego   = $_POST["juego"]   ?? "no respondido";
    $carrera = $_POST["carrera"] ?? "no respondido";
    $color   = $_POST["color"]   ?? "no elegido";
    $horario = $_POST["horario"] ?? "no respondido";
    $perros  = $_POST["perros"]  ?? "no respondido";
    $accion  = $_POST["accion"]  ?? "no respondido";
    $civil   = $_POST["civil"]   ?? "no respondido";

    // Formato de guardado
    $registro = date("Y-m-d H:i:s") . " | "
              . "$juego | $carrera | $color | "
              . "$horario | $perros | $accion | $civil\n";

    // Guardar en archivo
    file_put_contents("respuestas.txt", $registro, FILE_APPEND | LOCK_EX);

    echo "<h2>¡Gracias por responder!</h2>";
    echo "<p>Tus respuestas fueron guardadas correctamente.</p>";
}
?>
