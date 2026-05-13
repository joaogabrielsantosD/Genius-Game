| ![Logo](media/image1.png) | **UNIVERSIDADE FEDERAL DE PERNAMBUCO** <br/> CENTRO DE TECNOLOGIA E GEOCIÊNCIAS <br/> DEPARTAMENTO DE ELETRÔNICA E SISTEMAS <br/> DISCIPLINA DE ELETRÔNICA DIGITAL - 2026.1 |
|---|---|

DOCENTE RESPONSÁVEL: MARCO AURÉLIO BENEDETTI RODRIGUES

MONITORES: ALYSSON LUCAS, JOSÉ AUGUSTO, JULIANE SILVA, YURI VASCONCELOS

# Projeto 2: Genius

O Genius é um clássico jogo eletrônico de memória e agilidade, lançado nos anos 80, onde jogadores repetem sequências de luzes e sons. O objetivo é memorizar sequências cada vez mais longas, estimulando raciocínio e concentração com modos solo ou competitivo.

O jogo deverá ser implementado na placa FPGA da disciplina, utilizando exclusivamente a linguagem de descrição de hardware AHDL e a ferramenta Quartus. Pode-se utilizar as LMPs e macro funções do Quartus. O projeto deve possuir uma entidade de topo, construída em diagrama de blocos (.bdf), interligando no mínimo três módulos principais, como por exemplo: gerador de clock, controle do jogo e controlador do display de 7seg.

O sistema deverá reproduzir o funcionamento do jogo Genius utilizando os quatro botões como entradas, os quatro LEDs e os displays de sete segmentos da placa, como saídas visuais. A cada rodada, uma sequência aleatória de LEDs será exibida ao jogador, aumentando progressivamente de tamanho, começando por um. Após a exibição, um sinal sonoro deverá indicar o momento em que o jogador poderá repetir a sequência por meio dos botões.

Caso o jogador acerte a sequência, um som específico de sucesso deverá ser emitido e uma nova rodada será iniciada. Em caso de erro, outro som deverá indicar falha e a partida será encerrada. A pontuação obtida deverá ser mostrada temporariamente no display de 7seg e então retornar ao modo inicial de espera. Quando o sistema estiver em estado de espera (idle), o display deverá exibir o recorde armazenado do jogo.  
Enfatiza-se que o objetivo da prática é aplicar os conhecimentos sobre a modelagem de circuitos lógicos digitais utilizando AHDL.

## Definições Funcionais

- **a.** O sistema deve iniciar em modo espera, exibindo no display de 7seg o valor do recorde atual. Deve-se ter um botão para dar início ao jogo. A cada rodada o sistema deverá gerar e armazenar um número *pseudoaleatório*. Essa informação deve ser apresentada nos 4 LEDs da placa e nos displays de sete segmentos. Na primeira rodada será exibido 1 elemento, na segunda rodada 2 elementos, e assim, cumulativamente, sucessivamente, adicionando um novo elemento a cada rodada, até um total de 20 elementos.

- **b.** O número aleatório, a ser criado em cada rodada, pode ser resultante de um contador de módulo 4, com um clock de 50 MHz, que é inicializado ao ligar a placa (em paralelo com todo o jogo).

- **c.** Ao término da exibição da sequência nos LEDs e no display de sete segmentos, o sistema deverá indicar que o jogador pode iniciar sua resposta, esperando por um tempo, e finalizando o jogo caso não tenha a entrada do jogador.

- **d.** Caso o jogador repita corretamente toda a sequência apresentada, o sistema deverá emitir um som de acerto, incrementar a pontuação e iniciar automaticamente a próxima rodada. Caso o jogador erre qualquer elemento da sequência, o sistema deverá emitir um som de erro, exibir a pontuação final por alguns segundos no display de 7seg e retornar ao modo inicial de espera, apresentando o recorde no display.

- **e.** O sistema deverá armazenar o valor de recorde máximo obtido durante a utilização. Sempre que a pontuação atual superar o recorde anterior, esse valor deverá ser atualizado automaticamente. Enquanto o sistema estiver em modo espera, o display de 7seg deverá apresentar o recorde armazenado.

- **f.** O buzzer deverá reproduzir ao menos três sinais sonoros distintos: Som associado aos LEDs e ao acionamento dos displays de sete segmentos, durante a sequência, Som de acerto e Som de erro.

## Definições Estruturais

- **a.** Para gravação dos comandos, deve-se utilizar todos botões da placa com *debouncer*;

- **b.** Qualquer um dos quatro botões poderá ser utilizado para iniciar uma nova partida;

- **c.** Deve-se utilizar os quatro LEDs da placa e os displays de sete segmentos para exibição visual da sequência gerada pelo sistema e confirmação das entradas do jogador.

- **d.** Deve-se utilizar o buzzer para emissão dos sinais sonoros do jogo.

- **e.** Deve-se utilizar o display de 7seg para apresentação do recorde, pontuação e mensagens do sistema.

## Considerações Finais

1. **Deve-se** elaborar o relatório técnico completo detalhando todas as etapas de projeto realizadas para a solução do problema proposto no enunciado.

2. **Deve-se** entregar o relatório no *classroom* até 3 (três) horas antes da aula de apresentação juntamente com a pasta do projeto compactada em formato .rar ou .zip. Atrasos na submissão serão punidos com (-1 pt.) na nota de todos os integrantes do grupo. Não serão aceitos documentos enviados após a apresentação do respectivo grupo.

3. O relatório **deve** possuir no mínimo: introdução, desenvolvimento, manual de operação, resultados, discussão e conclusão. Conforme o documento "instruções para elaboração de relatórios técnicos", disponibilizado no *classroom*.

4. O relatório **deve** possuir imagens da placa na seção de resultados, evidenciando o funcionamento do sistema e ao submeter o trabalho no *classroom*, enviar um vídeo curto que comprove o funcionamento.

5. Durante a apresentação do projeto **deve-se** demonstrar o funcionamento do sistema e suas principais funcionalidades, ao vivo, conforme o enunciado do projeto, e sob demanda dos avaliadores.

6. **Não serão toleradas** cópias diretas de textos retirados da internet e/ou de trabalhos anteriores.