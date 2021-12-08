exports.enviar_email = function (serviço, email_autor, senha, destinatario, titulo, conteudo) {
    
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
    const dados = {
        from: remetente,
        to: destinatario,
        subject: titulo,
        text: conteudo
    }
    
    transporte.sendMail(dados, (err) => {
        if (err) {
            console.error(err)
        } else {
            console.log(`[+] - Email enviado.\nDe: ${remetente}\nPara: ${destinatario}\nTitulo: ${titulo}\nCorpo: ${dados.text}\n`)
        }
    })
}
