function validar_email (serviço, email_autor, senha) {
    const Express = require('express')
    const app = Express()
    const mailer = require('nodemailer')
    const remetente = email_autor
    mailer.getTestMessageUrl()
    const transporte = mailer.createTransport({
        service: serviço,
        auth: {
            user: remetente,
            pass: senha
        }
    })
    transporte.verify((error) => {
        if(error) {
            app.get('/', (req, res) => {
                
                res.send({"verify": false}).json
            }).listen(5001)
            console.log('[-] - O login falhou.')
        } else {
            app.get('/', (req, res) => {
                res.send({"verify": true}).json
            }).listen(5001)
            console.log('[+] - O login foi bem sucedido.')
        }
    })
}

const {email, senha} = require('../dados/credenciais.json')
validar_email('gmail', email, senha)