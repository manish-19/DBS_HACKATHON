    <?php
$servername = "localhost";
$username = "root";
$password = "21131141@lov";
$dbname = "formlogin";

$sql = "SELECT wmname,meettime,meetdate FROM meetdb";
$result = $conn->query($sql);

$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
          echo "name: " . $row["wmname"]. " - time: " . $row["meettime"]. "-date" . $row["meetdate"]. "<br>";
  }
} else {
  echo "0 results";
}
$conn->close();

?>