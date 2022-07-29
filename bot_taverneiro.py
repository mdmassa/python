from keep_alive import keep_alive
import random
import discord
import os
import requests
import json

client = discord.Client()

sad_words = ["triste", "depressão", "infelicidade", "desumilde", "miséria"]

starter_encouragements = [
  "Alegre-se, meu nobre... Beba um hidromel!",
  "Mantenha-se firme, guerreiro. A batalha ainda não acabou, tome uma cerveja por conta da casa! :beer:",
  "Para ser feliz existe apenas um caminho... Venha até a minha taverna que irei te dar a felicidade com o novo hidromel do oeste!"
]

tavern_drinks = [
  "Chegando na mesa uma caneca de cerveja bem gelada :beer:",
  "É pra já! O melhor hidromel da região :honey_pot:",
  "Essa Pitú é das boas, é a favorita do meu cliente Hoogh :tumbler_glass:",
  "Aqui está um bom vinho, meu nobre :wine_glass:",
  "Uma garrafa de champagne para comemorar... Saúde! :champagne:"
]

motivation_quotes = [
  "Tal qual um bêbado em busca de mais uma dose de hidromel. Grandes aventureiros caminharam em busca de novas aventuras, novas motivações e novas sensações.",         "Nunca esqueça, a verdadeira embriaguez está no momento em que você descobrirá o real sentido de viver... Se é que você vai encontrar, né?",
  "Nem sempre precisamos saber o real motivo das coisas. Às vezes, uma boa dose de hidromel pode guiar um humilde bebum a descobrir as maravilhas do universo.",
  "Uma vez, minha querida mãe me disse para preparar o melhor hidromel que este mundo já pode degustar. E sabe o que aconteceu? Eu não consegui... Porém, o que mais cativa as pessoas, não é ser único, é apenas saber como lidar com o que podemos proporcionar para o mundo, por isso mantenho minha taverna cheia todos os dias, servindo um hidromel comum. (Cof cof... Na verdade eu fiz o melhor hidromel sim, por isso a taverna é lotada...)"
]

advices_quotes = [
  "Não deixe dominar-se pelo passado, você vive no presente, caminhando para o futuro!",
  "Livre-se dos bajuladores. Mantenha perto de você pessoas que te avisem quando você erra.",
  "A verdade alivia mais do que machuca e estará sempre acima de qualquer falsidade.",
  "Não diga as coisas com pressa. Mais vale um silêncio certo que uma palavra errada!",
  "Cuide da sua saúde: se estiver boa, preserve-a. Se estiver instável, melhore-a. Se estiver além do que você possa fazer, peça uma cerveja!",
  "O caminho mais fácil, nem sempre é o melhor.",
  "Ao invés de chorar pelo leite derramado, aperte as tetas da vaca e baba mais um copo.",
  "Faz a tua ausência para que alguém sinta a sua falta. Mas não prolongue demais para que esse alguém não sinta que pode viver sem você...",
  "Jamais se iluda com uma declaração de amor, pois o verdadeiro amor jamais será declarado...",
  "Quando estiver vivendo grandes amores, lembre-se de seus melhores amigos.",
  "Quando te zoarem por depilar o toba, lembre-se: quem gosta de mato alto é cobra."
]

jokes = [
  "Sabe o que o melão estava fazendo de mãos dadas com o mamão perto de Copacabana? ||Levando o mamão papaya.||",
  "Por que o pinheiro não se perde na floresta? ||Porque ele tem um mapinha. HAHAHAHAHA Eu sei, sou hilário.||",
  "Sabe qual o nome do intestino do boi em espanhol? ||Intestino del gado HAHAHAHA ESSA FOI DE RACHAR O BICO, NÃO É VERDADE?! Agora compre uma cerveja.||"]

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('!motivacao'):
    await message.channel.send(random.choice(motivation_quotes))

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

  if msg.startswith('!bebida'):
    await message.channel.send(random.choice(tavern_drinks))

  if msg.startswith('!conselho'):
    await message.channel.send(random.choice(advices_quotes))

  if msg.startswith('!piada'):
    await message.channel.send(random.choice(jokes))

keep_alive()
client.run(os.getenv('TOKEN'))
