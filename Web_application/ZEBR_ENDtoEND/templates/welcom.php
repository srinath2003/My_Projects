<?php //welcom.php
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Surveillance App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 50;
            padding: 20;
            background-image: url('image1.jpeg');
            background-size: cover;
            background-position: center;
            color: #fff;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh; /* Makes the body take up the full height of the viewport */
            flex-direction: column;
        }
        nav {
            background-color: rgba(0, 0, 0, 0.7);
            padding: 15px;
            display: flex;
            justify-content: center;
            position: fixed;
            top: 0;
            width: 100%;
            z-index: 1000;
        }
        nav a {
            color: #fff;
            text-decoration: none;
            margin: 0 15px;
            font-size: 18px;
            transition: color 0.3s;
        }
        nav a:hover {
            color: #007bff;
        }
        h1 {
            margin-top: 50px;
            font-size: 2.5em;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }
        #videoFeed {
            width: 80%;
            max-width: 800px;
            margin: 20px auto;
            border: 2px solid #fff;
        }
        button {
            padding: 10px 20px;
            margin: 10px;
            font-size: 16px;
            cursor: pointer;
            background-color: #007bff;
            border: none;
            color: #fff;
            border-radius: 5px;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>

    <!-- Navigation Bar -->
    <nav>
        <a href="#">Home</a>
        <a href="#">Live Feed</a>
        <a href="#">Settings</a>
        <a href="#">About</a>
    </nav>

    <h1>Surveillance App</h1>

    <div>
        <button onclick="startVideoFeed()">Start Video Feed</button>
        <button onclick="stopVideoFeed()">Stop Video Feed</button>
    </div>

    <!-- Video Feed -->
    <img id="videoFeed" src="" alt="Video Feed" style="display:none;"> 

    <script>
        function startVideoFeed() {
            fetch('http://localhost:5000/start_feed', { method: 'POST' })
                .then(response => {
                    if (response.ok) {
                        const videoElement = document.getElementById('videoFeed');
                        videoElement.src = "http://localhost:5000/video_feed";
                        videoElement.style.display = "block"; // Show the video feed
                    } else {
                        console.error('Failed to start video feed');
                    }
                });
        }

        function stopVideoFeed() {
            fetch('http://localhost:5000/stop_feed', { method: 'POST' })
                .then(response => {
                    if (response.ok) {
                        const videoElement = document.getElementById('videoFeed');
                        videoElement.src = "";
                        videoElement.style.display = "none"; // Hide the video feed
                    } else {
                        console.error('Failed to stop video feed');
                    }
                });
        }
    </script>

</body>
</html>