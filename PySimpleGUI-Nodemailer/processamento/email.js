const { enviar_email } = require('./mailer.js')
const cred = require('../dados/credenciais.json')
const corpo = require('../dados/corpo.json')
console.log('[!] - Enviando email...')
enviar_email('gmail', cred.email, cred.senha, corpo.destinatario, corpo.titulo, corpo.conteudo)

