<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flight Booking System – Overbooking Simulation</title>
    < meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body {
            font-family: "Segoe UI", Tahoma, sans-serif;
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            margin: 0;
            padding: 0;
            color: #ffffff;
        }

        header {
            background-color: rgba(0, 0, 0, 0.4);
            padding: 30px;
            text-align: center;
        }

        header h1 {
            margin: 0;
            font-size: 32px;
            letter-spacing: 1px;
        }

        header p {
            margin-top: 10px;
            font-size: 16px;
            opacity: 0.9;
        }

        .container {
            max-width: 1000px;
            margin: 40px auto;
            padding: 20px;
        }

        .card {
            background-color: rgba(255, 255, 255, 0.08);
            border-radius: 12px;
            padding: 25px;
            margin-bottom: 30px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
        }

        .card h2 {
            margin-top: 0;
            color: #ffd369;
        }

        .card p {
            line-height: 1.7;
            font-size: 15px;
        }

        .flow {
            display: flex;
            justify-content: space-between;
            margin-top: 20px;
            gap: 20px;
            flex-wrap: wrap;
        }

        .box {
            flex: 1;
            min-width: 250px;
            background-color: rgba(0, 0, 0, 0.3);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }

        .box h3 {
            margin-top: 0;
            color: #4dd599;
        }

        .warning {
            color: #ff6b6b;
            font-weight: bold;
        }

        footer {
            text-align: center;
            padding: 20px;
            background-color: rgba(0, 0, 0, 0.4);
            font-size: 14px;
            opacity: 0.8;
        }

        footer span {
            color: #ffd369;
        }
    </style>
</head>
<body>

<header>
    <h1>Flight Booking System – Overbooking Case Study</h1>
    <p>Operating Systems Project | Critical Section & Race Condition</p>
</header>

<div class="container">

    <div class="card">
        <h2>📌 Real Case: Centrum Air Overbooking</h2>
        <p>
            Two passengers were unable to board their flight at Istanbul Airport because
            more tickets were sold than available seats. This situation is called
            <strong>overbooking</strong> and commonly occurs when concurrent booking requests
            access shared data without proper synchronization.
        </p>
    </div>

    <div class="card">
        <h2>⚙️ System Concept</h2>
        <p>
            In a flight booking system, the number of available seats is a
            <strong>shared resource</strong>. When multiple users attempt to book seats at the same time,
            a <strong>race condition</strong> may occur if the system does not protect the critical section.
        </p>

        <div class="flow">
            <div class="box">
                <h3>User A</h3>
                <p>Reads available seats</p>
                <p>Seat appears available</p>
            </div>

            <div class="box">
                <h3>User B</h3>
                <p>Reads available seats</p>
                <p>Seat appears available</p>
            </div>

            <div class="box">
                <h3 class="warning">Result</h3>
                <p>Both users book the same seat</p>
                <p class="warning">Overbooking happens ❌</p>
            </div>
        </div>
    </div>

    <div class="card">
        <h2>🔒 Solution: Synchronization</h2>
        <p>
            To prevent overbooking, the booking operation must be placed inside a
            <strong>critical section</strong> protected by a synchronization mechanism such as:
        </p>
        <ul>
            <li>Mutex Lock</li>
            <li>Semaphore</li>
            <li>Database Transaction</li>
        </ul>
        <p>
            This ensures that only <strong>one booking request</strong> can access and modify
            the seat count at a time.
        </p>
    </div>

    <div class="card">
        <h2>🧪 Backend Simulation</h2>
        <p>
            This project includes backend Python programs that demonstrate:
        </p>
        <ul>
            <li>Overbooking without synchronization</li>
            <li>Correct booking with mutex lock</li>
        </ul>
        <p>
            <strong>Note:</strong> This HTML page is only for visualization.
            All logic is implemented in the backend.
        </p>
    </div>

</div>

<footer>
    <p>
        Operating Systems Project | <span>Critical Section – Race Condition</span><br>
        Extra Project for Students at Risk of Failing
    </p>
</footer>

</body>
</html>
