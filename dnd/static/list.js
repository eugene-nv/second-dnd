new Vue(
    {
        el: "#list_app",
        data: {
            characters: []
        },
        created: function () {
            const vm = this;
            axios.get('/api/character/')
            .then(function (response){
                vm.characters = response.data
            })
        }
    }
)