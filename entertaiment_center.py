# encoding: utf-8
import movie_trailer_generator
import media
import simple_server

movies = []

movies.append(
	media.Movie("Doutor Estranho",
      "Um cirurgião desfigurado ganha uma nova chance em"
	  " sua vida quando um feiticeiro o treina para se "
	  "tornar o Mago Supremo.",
      "/images/doutor-estranho-poster-desktop.png",
      "https://youtu.be/aYs1WxZLGVI"))

movies.append(
	media.Movie("Galinha Pintadinha Mini na Telona",
      "Edição inédita e exclusiva da nova série da "
	  "Galinha Pintadinha Mini. O conteúdo mescla "
	  "historinhas narradas, atividades e as tradicionais "
	  "músicas, além de apresentar a Galinha e sua turma "
	  "com um novo design que promete encantar seus novos e antigos fãs.",
      "/images/a-galinha-pintadinha-mini-na-telona-poster-desktop.jpg",
      "https://youtu.be/imVgxEoVyv0"))

movies.append(
	media.Movie("Masha e o Urso",
      "Masha é uma pequena criança que não consegue parar quieta,"
	  "sempre arrumando uma forma de se meter em várias grandes "
	  "enrascadas. O único que pode salvá-la ou ajudá-la em suas "
	  "divertidas aventuras é Urso, um grande urso que vive na "
	  "floresta ao lado da casa de Masha e um grande amigo "
	  "da pequena menina.",
      "/images/masha-e-o-urso-poster-desktop.png",
      "https://www.youtube.com/watch?v=rA8wjaHW2a8&t=2s"))

movies.append(
	media.Movie("Sete Minutos Depois da Meia-Noite",
      "Conor é um garoto de 13 anos de idade, com muitos "
	  "problemas na vida. Seu pai é muito ausente, a mãe "
	  "sofre um um câncer em fase terminal, a avó é uma "
	  "megera, e ele é maltratado na escola pelos colegas. "
	  "No entanto, todas as noites Conor tem o mesmo sonho, "
	  "com uma gigantesca árvore que decide contar histórias "
	  "para ele, em troca de escutar as histórias do garoto. "
	  "Embora as conversas com a árvore tenham consequências "
	  "negativas na vida real, elas ajudam Conor a escapar das "
	  "dificuldades através do mundo da fantasia.",
      "/images/sete-minutos-depois-da-meia-noite-poster-desktop.jpg",
      "https://youtu.be/7oceCE4VjqI"))

movies.append(
	media.Movie("A Garota Desconhecida",
      "Jenny (Adele Haenel) é uma médica dedicada, que há três "
	  "meses passou a trabalhar na vaga deixada por um médico "
	  "veterano, que foi seu mentor. Bastante atenciosa com seus "
	  "pacientes, ela fica abalada ao saber sobre o falecimento "
	  "de uma jovem que procurou a clínica em que trabalha, mas "
	  "não conseguiu atendimento por ter chegado uma hora após o "
	  "horário de encerramento. Querendo saber mais sobre esta jovem, "
	  "ela passa a realizar uma investigação pessoal "
	  "em busca de sua identidade.",
      "/images/a-garota-desconhecida-poster-desktop.jpg",
      "https://youtu.be/WZJ1vxwOmFM"))

movies.append(
	media.Movie("Beleza Oculta",
      "Após uma tragédia pessoal, Howard (Will Smith) entra em depressão "
	  "e passa a escrever cartas para a Morte, o Tempo e o Amor - algo que "
	  "preocupa seus amigos. Mas o que parece impossível, se torna realidade "
	  "quando essas três partes do universo decidem responder. Morte "
	  "(Helen Mirren), Tempo (Jacob Latimore) e Amor (Keira Knightley) "
	  "vão tentar ensinar o valor da vida para o protagonista.",
      "/images/beleza-oculta-poster-desktop.png",
      "https://youtu.be/tj21dsJcp1w"))

movie_trailer_generator.open_movies_page(movies)
simple_server.start()