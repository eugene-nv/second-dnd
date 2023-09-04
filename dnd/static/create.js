new Vue(
    {
        el: "#create_app",
        data: {
            character: {
                race: '',
                klass: '',

                name: '',
                gender: '',
                ideology: '',

                portrait: '',

                strength: 0,
                dexterity: 0,
                constitution: 0,
                intelligence: 0,
                wisdom: 0,
                charisma: 0,
              }
        },
        methods: {
            addForm() {
                {
                    axios
                      .post('/api/character/', this.character
                      )
                      .then(response => {
                        console.log('data', response.data)
                      })
                      .catch(error => {
                        console.log('error', error)
                      })

                }
            },

            clearForm() {
              this.character = {
                name: '',
                gender: '',
                race: '',
                klass: '',
                level: 0,
                description: ''
              }
        }
    }
}
)