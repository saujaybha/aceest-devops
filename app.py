from flask import Flask, jsonify, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return jsonify({
        "app": "ACEest Fitness",
        "version": "v4.0",
        "status": "running"
    })

# Sample client data (in-memory for now)
clients = []

# Add client
@app.route('/add_client', methods=['POST'])
def add_client():
    data = request.get_json()
    
    client = {
        "name": data.get("name"),
        "age": data.get("age"),
        "weight": data.get("weight"),
        "program": data.get("program")
    }
    
    clients.append(client)
    
    return jsonify({"message": "Client added", "client": client})

# Get all clients
@app.route('/clients', methods=['GET'])
def get_clients():
    return jsonify(clients)

# Health check (important for Docker/K8s)
@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
