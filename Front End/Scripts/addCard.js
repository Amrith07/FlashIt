let app = new Vue({
    el: "#app",
    data: {
        msg:"",
        key:"",
        answer:"",
        difficulty:""
    },
    methods: {
        addCard(){
            
            console.log(this.key);
            console.log(this.answer);
            console.log(this.difficulty);

            var headers = new Headers();
            headers.append("Authorization", "Bearer " + localStorage.getItem("token"));
            headers.append("Content-Type", "application/json");

            var jsonContent = JSON.stringify({
                "key": this.key,
                "answer": this.answer,
                "difficulty": this.difficulty
            });

            var requestOptions = {
                method: 'POST',
                headers: headers,
                body: jsonContent,
                redirect: 'follow'
            };

            fetch("http://127.0.0.1:5000/newCard", requestOptions)
                .then(response => response.json())
                .catch(error => console.log('error', error));
        }
    }
})