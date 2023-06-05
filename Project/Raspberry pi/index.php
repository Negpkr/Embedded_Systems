<html>
<head>
<meta name="viewport" content="width=device-width" />
<title>Negin watering system</title>
</head>
       <body>
       <center><h1>Negin watering system</h1>      
         <form method="get" action="index.php">               
            <input type="submit" style = "font-size: 14 pt" value="Plant 1 OFF" name="off1">
            <input type="submit" style = "font-size: 14 pt" value="Plant 1 ON" name="on1">
            <br /> <br />
            <input type="submit" style = "font-size: 14 pt" value="Plant 2 OFF" name="off2">
            <input type="submit" style = "font-size: 14 pt" value="Plant 2 ON" name="on2">
         </form>​​​
         
                         </center>
<?php
    shell_exec("/usr/local/bin/gpio -g mode 17 out");
    if(isset($_GET['off1']))
        {
                        echo "pump 1 is off";
                        shell_exec("/usr/local/bin/gpio -g write 17 0");
        }
            else if(isset($_GET['on1']))
            {
                        echo "pump 1 is on";
                        shell_exec("/usr/local/bin/gpio -g write 17 1");
            }
   shell_exec("/usr/local/bin/gpio -g mode 27 out");
    if(isset($_GET['off2']))
        {
                        echo "pump 2 is off";
                        shell_exec("/usr/local/bin/gpio -g write 27 0");
        }
            else if(isset($_GET['on2']))
            {
                        echo "pump 2 is on";
                        shell_exec("/usr/local/bin/gpio -g write 27 1");
            }              
?>
   </body>
</html>
