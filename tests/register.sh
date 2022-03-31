curl \
    --header "Content-Type: application/json" \
    --request POST \
    --data '{"username":"johndoe","password":"johndoe2022!","email":"johndoe@example.com"}' \
    http://127.0.0.1:5000/users/register \

curl \
    --header "Content-Type: application/json" \
    --request POST \
    --data '{"username":"janedoe","password":"janedoe2022!","email":"janedoe@example.com"}' \
    http://127.0.0.1:5000/users/register \