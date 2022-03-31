curl \
    --header "Content-Type: application/json" \
    --request POST \
    --data '{"email":"janedoe@example.com","password":"janedoe2022!"}' \
    http://127.0.0.1:5000/users/login \