import pygame
from pygame.locals import *
from pygame import mixer

from youssef_class import *
from pier_class import *
from raul_class import *
from fabiano_class import *
import sound

import drawer as dw
from data import *

class Dialogues():
    def __init__(self):
        self.number_of_dialogue = 0

        self.text_of_dialogue = []
        self.image_of_dialogue = []
        self.background = []

        self.show_gui = True

        self.text_visualized = 0
        self.image_visualized = 0
        self.background_visualized = 0


    def set_dialogue(self, number_of_dialogue):
        self.number_of_dialogue = number_of_dialogue
        if number_of_dialogue == 0:
            text_of_dialogue_0 = [
            ["Premi 'Enter' per iniziare",""],
            ["Fabiano","Salve! Benvenuto nella demo del nostro gioco."],
            ["Raul","Noi siamo i creatori, vi spiegheremo in breve come giocare."],
            ["Fabiano","In questa demo affronterai un solo boss, giusto per avere un'infarinatura delle meccaniche prima dell’uscita ufficiale."],
            ["Raul","Dovrai comandare quattro personaggi, ognuno con le sue caratteristiche."],
            ["Raul","Ogni personaggio ha a disposizione 3 skills e 2 friends, oltre a qualche item condiviso con la squadra."],
            ["Fabiano","Le skill sono abilità che consumano mana, sono diverse da personaggio a personaggio in base al loro stile di gioco."],
            ["Raul","Mentre io ho abilità offensive, Pier usa abilità perlopiù difensive e di supporto. Youssef è un misto moderato tra offensive e difensive, mentre Fabiano sviluppa buone abilità di supporto."],
            ["Fabiano","I friends possono essere utili perché offrono delle abilità utilizzabili una singola volta, ma sanno liberarti da cattive situazioni."],
            ["Raul","Gli items non servono spiegarli. Fai attenzione che l'inventario è condiviso e gli item sono limitati."],
            ["Fabiano","Infine i personaggi hanno accesso a  \"recover \", una  \"abilità\" di recupero che permetterà di ripristinare parte del mana."],
            ["Raul","Fabiano! Prima dobbiamo spiegargli le statistiche!"],
            ["Fabiano","Giusto! Le statistiche sono dei  \"punti\" che indicano quanto un personaggio sia forte in qualcosa."],
            ["Raul","Per esempio io ho tanto attacco ma ho poca velocità. Mentre Pier ha tanta difesa ma poca evasione."],
            ["",""], # 14
            ["Fabiano","Abbiamo cercato di rendere il gioco più accessibile possibile, ogni cosa ha una sua descrizione con il suo effetto, basta leggere."],
            ["Raul","Detto questo, noi vi lasciamo al resto."],
            ["Fabiano","Non ti sei dimenticato tipo la cosa che influenzerà di più il gioco?"],
            ["Raul","Cosa? Non dovrebbe essere rimasto altro."],
            ["Fabiano","Arrabbiato... Triste... ti dice qualcosa?"],
            ["Raul","Vero! Ogni personaggio durante il combattimento può provare emozioni differenti che vengono causati da varie abilità, friends o item."],
            ["Fabiano","Le emozioni aumentano determinate statistiche, ma diminuiscono altre. Inoltre fungono da \"tipo dinamico\"."],
            ["Raul","Fabiano, che cosa stai dicendo?"],
            ["Fabiano","È un termine che ho pensato io. Le emozioni continuano a cambiare durante il turno, per questo le chiamo dinamiche. Mentre le chiamo tipo perché condividono il famoso concetto Pokémon: Erba batte acqua che batte fuoco che batte erba."],
            ["",""], # 24
            ["Raul","I friends possono tornare utili certe volte per manipolare le emozioni, se avete difficoltà, provate a leggere qualche effetto."],
            ["Fabiano","Anche gli item hanno effetti del genere e pure qualche abilità."],
            ["Raul","Ok stiamo parlando troppo. Facciamolo giocare."],
            ["Fabiano","Va bene... (Piccolo suggerimento: prova ad usare la mia skill Benevento per qualche turno, rendi me euforico e il nemico arrabbiato, poi usa Pestata, non te ne pentirai!)."],
            ["",""]
            ]
            image_of_dialogue_0 = [NOTHING,FABIANO,RAUL]
            background_0 = ["None",STATS_EXPLANATION, EMOTION_EXPLANATION]   
        
            self.text_of_dialogue = text_of_dialogue_0
            self.image_of_dialogue = image_of_dialogue_0
            self.background = background_0

        if number_of_dialogue == 1:
            text_of_dialogue_1 = [
                # *Scena due che cadono*
                ["",""],

                ["Raul","..."],
                [ "Raul ", "D-dove sono? "],
                [ "Raul ", "Oh, Youssef, sveglia! "],
                [ "Youssef ", "… Uh, Cosa? "],
                [ "Raul ", "Svegliati! Uhh… ma dove siamo…? "],
                [ "Youssef ", "Mhhh… Che è 'sto posto? "],
                [ "Raul ", "Non ne ho idea. Eravamo sulla barca a Venezia, cosa è successo? "],
                [ "Youssef ", "Mi ricordo solo che ci siamo scontrati con un’onda strana che ci ha ribaltato le barche. Poi siamo… affogati? "],
                [ "Raul ", "Allora siamo mo- "],
                [ "??? ", "Altri due eroi sono stati rinvenuti, in tutto sono… quattro? Penso di aver fatto male i conti. "],
                [ "Youssef ", "Chi ha parlato? "],
                [ "??? ", "Sono il Leone Alato, protettore di Venezia. Seguite la scia luminosa, avete dei compagni. "],
                [ "Youssef ", "Compagni? Quindi non siamo finiti solo noi due qui. "],
                [ "...", "..."],
                [ "Fabiano ", "Eccovi! "],
                [ "Raul ", "Fabiano? Uh, Pier? Anche voi qui? "],
                [ "Pier ", "Sì, sto’ posto sembra un rip-off di Atlantide. "],
                [ "Leone Alato ", "Roar… non è un rip-off (ma proprio questi dovevo trovare?). Siete a Subnezia, il paese subacqueo sotto la città di Venezia "],
                [ "Fabiano ", "Ookay… ma noi saremmo in gita e dovremmo tornare lassù. "],
                [ "Leone Alato ", "Oh, questo è impossibile, avete passato la \"prova del gondoliere\", siete gli unici mortali presenti qui. "],
                [ "Raul ", "Aspetta un secondo, in che senso \"gli unici mortali\"? "],
                [ "Leone Alato ", "Gli abitanti di Subnezia sono le anime morte nel perimetro della vecchia repubblica veneziana. "],
                [ "Pier ", "Aspetta, poi cosa intendi con sta’ \"prova del gondoliere\"? Noi non abbiamo fatto nulla "]
                [ "Leone Alato ", "Non posso svelare i requisiti per passarla, altrimenti pure i nostri spettatori tenteranno, non posso permettere che entrino degli sciocchi. "],
                [ "Fabiano ", " \’’spettatori\’’? Stai rompendo una quarta parete o cosa? "],
                [ "Leone Alato ", "Ma no, parlo degli studiosi del posto. L'esistenza di questo luogo è nota da decenni e sono riusciti a mettersi in contatto con il Re, cercando di farlo ragionare invano. "],
                [ "Leone Alato ", "Il Re è Paolo Lucio Anafesto, il primo Doge, l’innalzamento dell’acqua è opera sua, come anche la creazione di Subnezia stessa. "]
                [ "Raul ", "Dobbiamo fargliela pagare allora. "]
                [ "Leone Alato ", "Bravo, voi eroi avete il compito di annientare il re, se lo farete, potrete ritornare alle vostre vite quotidiane. O meglio alla vostra gita. "]
                [ "Youssef ", "Si menaaa. "],
                [ "Leone Alato ", "Per questo vi ho convocati. Ma prima di andare da lui, abbiamo bisogno di alleati. Prima non ho detto propriamente la verità, non siete gli unici mortali. "]
                [ "Fabiano ", "Mh? Cosa intendi? "]
                [ "Leone Alato ", "Ci sono altri individui che vengono dal vostro mondo che sono stati catturati dai governanti dei 4 regni di Subnezia, per salvarli dovrete sconfiggere anche questi. Hanno anche loro dei poteri che vi permetteranno di darvi una mano. "]
                [ "Pier ", "Poteri? Cosa inten- Cosa sono quelle?! "]
                [ "Leone Alato ", "Sono armi magiche. Pensavi vi avrei fatto combattere a mani nude? "],
                [ "Fabiano ", "Ah ok, stavo già per andarmene "],
                [ "Leone Alato", "Al ragazzo basso regalerò la Staffa di Merlino, capace di scagliare magie quasi in autonomia."]
                [ "Raul ", "Classe mago, baby. "]
                [ "Leone Alato ", "Al ragazzo deboluccio darò i Bracciali dei Monsoni, con questi hai la libertà di governare le masse d’aria circostanti e di dare il ritmo al party. "]
                [ "Fabiano: Non siamo sott’acqua? "],
                [ "Leone Alato ", "Questa zona è coperta dall’acqua, se vedi ci sono delle barriere che impediscono all’acqua di raggiungere la zona. Come spieghi il fatto di star respirando? "],
                [ "Youssef ",  "Eh, Fabiano… "],
                [ "Fabiano ", "... Ok. "]
                [ "Leone Alato ", "Al ragazzo alto consegnerò il Tomo della Fenice, contiene magie legate al fuoco da usare sui compagni. Non vi dovrebbero arrostire, tu però stai attento comunque. "],
                [ "Pier ", "Ho capito, mi divertirò moltissimo. "]
                [ "Fabiano ", "Perché dai a lui quello più pericoloso? "]
                ["Pier","Shhh, andrà tutto bene. "]
                [ "Leone Alato ", "Infine, a te consegnerò la Palla Meteora, un pallone in grado di poter creare grandi catastrofi, ma soltanto se ne sei degno. "]
                [ "Youssef ", "Non mi sembra avere chissà che poteri. C’è già Raul che stava rischiando di esplodere o Pier che sta già lanciando fiamme… "],
                [ "Youssef ", "Sei sicuro sia questa? Anche lanciandola mi sembra una normal- "],
                [ "Leone Alato ", "Ahhh! Santo mare! Me ne spetava solo tre, sa voto che te diga? Tiraghe ‘na sbalona’ e te vedi che te lo fe’ volar via! "],
                [ "Youssef ", "Se ci pensi. "],
                [ "Leone Alato ", "Vi servirà un addestramento prima di affrontare i guardiani "],
                [ "Leone Alato ",  "Vi spiegherò come si combatte, tutorial offerto da Leonzulla! "],
                [ "Pier ","(Leonzulla? …) "],

                # TUTORIAL
                ["",""],

                ["Leone Alato", "questo è quello che dovete sapere per ora, vi porto dal primo governante."],
                [ "Leone Alato ", "Prima area: \"Gameplay Courtyard\", qui ci sono le anime che hanno preso forma dei personaggi dei videogiochi. "],
                [ "Raul ", "\’’prendono forma\’’? Le anime sono anime. "],
                [ "Leone Alato ", "A Subnezia si tramutano in base ai propri ricordi in vita. "],
                [ "Leone Alato ", "In questo luogo giacciono i videogiocatori, tramutati nel proprio personaggio preferito. "],
                [ "Youssef ", "Quindi chi sarà il governatore? Forse Doomslayer? Kratos? "],
                [ "Leone Alato ", "Assolutamente no! Nessuno di questi è degno, sono troppo deboli. "],
                [ "Youssef ", "E chi è allora? L’Hog Rider di Clash Royale? "],

                # *Appare lo sprite del mago elettrico *
                ["",""],

                [ "Leone Alato ", "Lui è il governante. "],
                [ "Pier ", "Beh ci sei andato vicino. (Ma che ca-) "],
                [ "Raul ", "(Il mio idolo!) "],
                [ "Leone Alato ", "Questa è la prima prova, sembra debole ma non fatevi ingannare, vi assisterò con degli utili strumenti. Fatevi valere, eroi! "],
                [ "Fabiano ", "(Cosa abbiamo fatto per meritarci questo?) "],

                ]
            self.text_of_dialogue = text_of_dialogue_1
            
        if number_of_dialogue == 2:
            text_of_dialogue_2 = [
                [ "Raul ", "Fulmini contro fulmini! È stato bello! "],
                [ "Youssef ", "Certo, prendere a pallonate la gente è molto divertente. "],
                [ "Leone Alato ", "Bene, seguitemi che abbiamo ancora molto da fare. "],
                [ "… ", "... "],
                [ "Pier ", "Perché siamo in questa prigione? Sono stanco di camminare."],
                [ "Fabiano ", "Pier, non ricordi? Non siamo gli unici che combatteranno. Avremo degli alleati che ci aiuteranno. "],
                [ "Leone Alato ", "Ah, allora mi ascoltavate, che gentili. Piuttosto, questa è la cella. "],
                [ "Fabiano ", "Eh? Pol?! "],
                [ "Youssef ", "Guarda meglio, ci sono anche altri! "],
                [ "Pier ", "Cappe, Ilaria… e Cristian anche. Che ci fanno loro qui? "],
                [ "Cappe ", "È successo un casino qui, ci siamo ritrovati davanti al coso di Clash Royale che ci ha sbattuti qui in prigione. "],
                [ "Leone Alato ", "I governanti come avete visto sono aggressivi e vogliono proteggere Paolo Lucio Anafesto. "]
                [ "Raul ", "Non importa, almeno non siamo solo noi quattro qui sotto! "],
                [ "Pol ", "Effettivamente non ci ritroviamo in una bella situazione, ma almeno dovremmo esserci tutti qui. Dobbiamo sbrigarci a trovare anche gli altri. "],
                [ "Cristian ", "Intanto fateci uscire che c’è troppa puzza qua. "],
                [ "Leone Alato ", "Certamente. "],
                [ "Leone Alato ", "Adesso che vi abbiamo liberati, proseguiamo alla seconda zona. "],

                # *Entrano nella seconda area*
                ["",""],
                [ "Ilaria ", "Quindi qui troveremo altre persone rinchiuse? "],
                [ "Leone Alato ", "Certo, ma possiamo liberarle soltanto dopo aver sconfitto il governante. Non vi rovino la sorpresa. "],
                [ "Pier ", "Pare un paesaggio fiabesco. "],
                [ "Youssef ", "Il paesaggio è affascinante, ma aspetta, cos'è quell'uovo? "],
                [ "Raul ", "Humpty Dumpty? "],
                [ "Leone Alato ", "Il governante della seconda zona. "],
                [ "Cristian ", "Ma scusa quell’uovo lì? "],
                [ "Humpty Dumpty ", "Che ammasso di falliti, voi vorreste affrontare Lucio? Siete solo bambini hahahaha. E sembrate deboli, mooolto deboli! "],
                [ "Pier ", "…Quanto mi fa inc- "],
                [ "Fabiano ", "Ehi! "],
                [ "Pier ", "Cosa? "],
                [ "Fabiano ", "Nun dire le parolacc! Siamo in un progetto che dobbiamo anche mostrare a scuola! "],
                [ "Youssef ", "Scuuuuus? "],
                [ "Ilaria ", "Aspetta, ma hai appena rotto la quarta parete? "],
                [ "Fabiano ", "Uhm… forse. "],
                [ "Cappe ", "Ma a me sembra troppo realistico per essere dentro un gioco. "],
                [ "Pol ", "Ma troppo realistico di cosa?! "],
                [ "Humpty Dumpty ", "Urgh… SMETTETELA DI IGNORARMI E COMBATTETE! "],
                [ "Leone Alato ", "Roar! Non pensare di poterli battere! Continuate a chiedermi aiuto se vi servono dei strumenti, ne ho di nuovi ad ogni incontro. "]

            ]
            self.text_of_dialogue = text_of_dialogue_2
        if number_of_dialogue == 3:
            text_of_dialogue_3 = [
                [ "Youssef ", "Ti abbiamo sbattuto come un uovo! "],
                [ "Pier ", "Qualcuno vuole una frittata? "],
                [ "Raul ", "Me son roto i'ovi… andiamo avanti "],
                [ "Cristian ", "Meglio che mi avete fatto cringiare con le vostre battute "],
                [ "Leone Alato ", "La prossima prigione è di qua, seguitemi. "],
                ["Pol","Chissà chi ritroveremo qui ora. Spero altri della classe, sennò chissà che fine avranno fatto."],
                ["Leone Alato","Eccone altri quattro, dovrebbero essere tutti vostri compagni."],
                ["Ilaria","Perché state tutti ridendo?"],
                ["Stefan","No vabbè cioè scusa un attimo. No perché qua Humpty Dumpty quell'uovo maledetto mi avrà preso in giro per tutto il tempo per come sono vestito."],
                ["Youssef","Beh, sei adorabile, su quello non ci piove."],
                ["Stefan","Sì, ma che cacchio-"],
                ["Anastasia","Guarda che sei molto alla moda, e per fortuna che non hai iniziato ad attaccarlo che sennò facevamo una brutta fine."],
                ["Leone Alato","... Bene, ora siete liberi."],
                ["Trentin","Ma avete visto cos'ha Noce?"],
                ["Cappe","Lo volevo io! Guarda a me che schifo che ho ricevuto! Magari avessi un cecchino."]
                ["Noce","Sì, ma ha un solo colpo e mi ritorna dopo chissà quanto tempo."],
                ["Trentin","Comunque mancano ancora tanti, dove sono gli altri?"],
                ["Leone Alato","Dobbiamo dirigerci in un'altra zona. Probabilmente lì troveremo tutti i vostri alleati, muoviamoci."],

                # *Terza zona*
                ["",""],

                ["Leone Alato","Questa è il piccolo regno del Giappone. State attenti, ci sono rovine qua e là a causa di una feroce guerra."],
                ["Raul","Hiroshima?"],
                ["Leone Alato","Non è esattamente così ma si avvicina. Il nuovo governante ha gettato una bomba ad idrogeno per sconfiggere il vecchio governante."],
                ["Cappe","E chi è? Doraemon?"],
                ["Noce","C'è qui Doraemon. Lo vedo in quella casa laggiù."],
                ["Leone Alato","La casa del Governante: Doraemon. Colui che sconfisse il precedente governante: l'EVA01."],
                ["Fabiano","Ma che-"],
                ["Ilaria","Sarà dura combattere contro Doraemon, come faremo ad attaccarlo?"],
                ["Stefan","Con le cinghiate, ovviamente!"],
                ["Pol","Un banco nei denti fa più effetto. Dai sbrighiamocela."],
                ["Doraemon","So perché siete giunti qui e non posso nemmeno dirvi di fermarvi. Però posso convincervi…"],
                ["Anastasia","E con cosa…?"],
                ["Doraemon","Volete viaggiare nel tempo? Oppure volare in giro?"],
                ["Anastasia","Dai non voglio più affrontarlo. Non me ne faccio niente di questo potere! Fatemi volare!"],
                ["Youssef","Fatemi picchiare sto gatto vi prego."]

                    ]
            self.text_of_dialogue = text_of_dialogue_3
        if number_of_dialogue == 4:
            text_of_dialogue_4 = [
                ["Pier","Una. bomba. ad. idrogeno. SERIAMENTE?!"],
                ["Noce","Ci aveva avvertito…"],
                ["Raul","State bene voi? Io no."],
                ["Cappe","Non so neanche come faccio ancora ad essere vivo."],
                ["Leone Alato","Tranquilli, vi sistemo tutti io. Complimenti eroi, non era facile."],
                ["Fabiano","(Alla faccia!)"],
                ["...","..."],
                ["Youssef","Girovagando per le cata-combe… hey, hey."],
                ["Stefan","Uhmm, Leone?"],
                ["Leone Alato","Sì, Leone il cane fifone. Chiamatemi Leone Alato, portatemi un po' di rispetto. Cosa ti serve."],
                ["Stefan","Mi scusi Egregio Signor Leone Alato, ma penso che Youssef abbia qualche botta ancora da prima con la bomba."],
                ["Youssef","Ah, nono, sto benissimo. Mai stato meglio. Oh, Diego!"],
                ["Diego","Ma…! Non ce la facevo più a stare qui, se non fosse per il PRADE."],
                ["Prade","Oh, ma che fatica… Stare qui è proprio 'na roba con tutti sti giapponesi…"],
                ["Pol","Forza Roma…"],
                # *animazione di forza roma*
                ["",""],
                ["Raul","Oh ma quanta carica! SPACCO TUTTO."],
                ["Borin","Io non ho ancora ben capito questa cosa dei poteri. Ci hanno dato cose strane che hanno effetti ancora più strani. Guardate che ha Diego."],
                ["Diego","Eh? Ah, no io non ho nulla di interessante. Solo un po' di camomilla."],
                ["Prade","Sisì camomilla. Guarda che si vede che non è camomilla."],
                ["Pol","È il caso, no?"],
                ["Diego","Beh, KIARO"],
                ["Damonte","Finalmente fuori che non ce la facevo più."]
                ["Cappe","Ma, scusate, questa 'camomilla', l'avete assagg-"],
                ["Damonte","S-"],
                ["Diego, Prade, Borin","ASSOLUTAMENTE NO!"],
                ["Fabiano","Dio mio, che ce ne facciamo…"],
                ["Leone Alato","Ti ricordo che ho dato io questi poteri. Ti assicuro che non è camomilla, ma giuro che servirà in battaglia e che la dovrai assumere."],
                ["Raul","Dai! Ti obbligo a prenderla se dovremo!"],

                # *cambio di zona*
                ["",""],

                ["Leone Alato","Ora che siamo al completo, dobbiamo annientare l'ultimo governante, poi Paolo Lucio Anafesto e infine arriveremo all'epilogo. Come vi sentite?"],
                ["Damonte","Stanco!"],
                ["Ilaria","Ma se ti sei appena aggiunto a noi…"],
                ["Noce","Dopo un po' ti abitui. Ormai sono inseparabile dal mio cecchino"],
                ["Pol","E Stefan dal suo abito-"],
                ["Stefan","Oh! Guarda che le prendi eh."],
                ["Raul","Non cominciare a fare polemica, Anghel."],
                ["Pier","Chi dobbiamo affrontare ora?"],
                ["Leone Alato","Questa zona rappresenta una sfida molto ardua. Quarta zona: Il Grande Passaggio."],
                ["Cappe","Fa venire i brividi… Chi è il governante, Slenderman?"],
                ["Varie voci con tono basso","Voi…"],
                ["Youssef","Mi sto per cacare nei pantaloni, non fate brutti scherzi."],
                ["???","Ombrello…"],
                ["???","Innocenza…"],
                ["???","Ripetere…"],
                ["???","Assenze…"],
                ["Borin","Ma chi sono questi? Ombrello? Ma che-"],
                ["Pol","Non vorrei dirlo, ma siamo circondati."],
                ["Cristian","E chi sono questi? Ma andatevene via!"],
                ["Varie voci con tono basso","Ohh, non ce ne andremo via. Sarete voi a venire con noi."],
                ["Leone Alato","Questa zona contiene tutte le persone che sono state dimenticate. Avete una buona esperienza di combattimento, se riuscirete a cavarvela davanti a ciò che avete lasciato indietro, potrete affrontare la sfida più grossa."],
                ["Pier","Perché ci deve sempre essere la parte inquietante in ogni gioco…"],
                ["Fabiano","Finché mancano i jumpscare, lo accetto."],
                ["Raul","Me li sognerò per un anno penso."],
                ["Amalgamato","Sentirete tutti i nostri lamenti e infine diverrete parte di noi."]
                ]
            self.text_of_dialogue = text_of_dialogue_4
        if number_of_dialogue == 5:
            text_of_dialogue_5 = [
                ["Damonte","È finita?"],
                ["Ilaria","Non lo vedo più. Però davvero che botta di emozioni."],
                ["Youssef","Se ne è andato, però c'è qualche spirito ancora attorno a noi."],
                ["Cappe","Cosa? Mohammed?"],
                ["Mohammed","Uh, eh- non attaccarci! Volevamo aiutarvi per la vostra impresa."],
                ["Stefan","Attaccandoci? O volevate allenarci?"],
                ["???","Non hai capito. Lo spirito era mosso dall'insieme di tutti. Non volevamo attaccarvi dall'inizio."],
                ["Fabiano","Kevin?!"],
                ["???","Ora vogliamo unirvi a voi sembra che dobbiate affrontare Anafesto."],
                ["Pier","Gonzato?!"],
                ["Ciudin","Non ho capito perché mi avete voluto includere."],
                ["Kevin","Gli altri non volevano ascoltare, ci siamo divisi appena ci siamo indeboliti abbastanza."],
                ["Pol","Sempre bello vedervi."],
                ["Stefan","Quindi l'ombrello, alla fine l'hai cercato."],
                ["Ciudin","Ho soltanto memoria di quando ero con voi. Infatti vi ricordo molto più diversi e numerosi. Però effettivamente l'ombrello ora che ci penso che fine ha fatto?"],
                ["Youssef","Uh, no niente. Non preoccuparti te l'avevamo ridato."],
                ["Leone Alato","Visto che parli di ombrello e sembrate essere veramente disposti ad aiutarli. Ecco qua dei strumenti per voi."]
                ["Ciudin","È il mio ombrello questo! Che me ne dovrei fare"],
                ["Youssef","Ho un'idea, passamelo quando serve. Ne farò buon uso."],
                ["Kevin","Un megafono? Cosa me ne faccio scusa? Vabbè vi dirò qualcosa dai."],
                ["Cappe","Dai raga! Siete pronti che ora c'è il bossss…"],
                ["Noce","Non c'è mai una pausa. Però devo dire che non è male questa avventura."],
                ["Leone Alato","Dai, dobbiamo dirigerci in fretta. Seguitemi!"],

                # *ultima zona*
                ["",""],

                ["Pier","Cosa succede se non ce la facciamo a sconfiggerlo."],
                ["Leone Alato","Divertente come non vi siete posti questa domanda prima mentre eravate soli che adesso siete in un gruppo davvero numeroso"],
                ["Anastasia","Dai entriamo e finiamola. Anche se mi dispiacerà non vedere più Stefan così."],
                ["Raul","Eddai, apriamo le porte per la sala del trono e battiamolo!"],

                # *Scena Anafesto*
                ["",""],

                ["Paolo Lucio Anafesto","E alla fine siete giunti qui e non finiti nelle mani dei miei governanti. Un peccato, davvero, che alla fine siano tutti stati eliminati. Me ne farò una ragione."],
                ["Paolo Lucio Anafesto","Vi sistemerò tutti uno alla volta, compreso te, Leone Alato! Non pensare che scapperai questa volta."],
                ["Pier","No vabbè ma che figo è quel poseidone lì?"],
                ["Youssef","Ma ti immagini che grigliata su quell'addome."],
                ["Ilaria","Ragazzi… è il boss, dovremmo affrontarlo."],
                ["Paolo Lucio Anafesto","È per caso una provocazione. Stai provocando il sovrano di Subnezia… Paolo Lucio Anafesto?!"],
                ["Prade","Non ce la faccio ad ascoltarlo qua, davvero mi fa troppo ridere come parla."],
                ["Paolo Lucio Anafesto","Siete stolti, la vostra non è lontanamente audacia. Nessuno uscirà vivo da qui."],
                ["Diego","Questo si crede tanto forte, ma secondo me: tutto fumo niente arrosto."],
                ["Paolo Lucio Anafesto","Insolenti!"]
                ]
            self.text_of_dialogue = text_of_dialogue_5
        if number_of_dialogue == 6:
            text_of_dialogue_6 = [
                ["dialogo n.7","Mi mangio il sushi con il pesce agagaga"],
                ["",""], # 24
                ["Raul","I friends possono tornare utili certe volte per manipolare le emozioni, se avete difficoltà, provate a leggere qualche effetto."],
                ["Fabiano","Anche gli item hanno effetti del genere e pure qualche abilità."],
                ["Raul","Ok stiamo parlando troppo. Facciamolo giocare."],
                ["Fabiano","Va bene... (Piccolo suggerimento: prova ad usare la mia skill Benevento per qualche turno, rendi me euforico e il nemico arrabbiato, poi usa Pestata, non te ne pentirai!)."],
                ["",""]
            ]
            self.text_of_dialogue = text_of_dialogue_6
        # print("")


    def dialogue(self, input):
        # Disegno il background
        dw.dialogue_bg(self.background[self.background_visualized])
        # Disegno GUI
        if self.show_gui:
            dw.dialogue_gui(self.image_of_dialogue[self.image_visualized])
        
        if dw.dialogue_box.current_width == dw.dialogue_box.desired_width:
            dw.title_and_text_action(str(self.text_of_dialogue[self.text_visualized][0]),(WHITE),self.text_of_dialogue[self.text_visualized][1], int(FONT_SIZE*1.3), (SPACING*3, HEIGHT-dw.dialogue_box.height), WIDTH-SPACING*5)
            dw.text_given_last_coordinates('Premi "Enter" per continuare.', int(FONT_SIZE*1.3), ( (WIDTH-(SPACING*2)-BOX_BORDER), HEIGHT-(SPACING*2)-BOX_BORDER), MANA_INSIDE)
            #WIDTH-SPACING*4, int(BOX_HEIGHT*1.2),  SPACING*2, SPACING,

            if input == "return":
                pygame.mixer.Sound.play(sound.CONFIRM)
                self.text_visualized += 1
                dw.dialogue_box.in_closure = True
                
                if self.number_of_dialogue == 0:
                    if self.text_of_dialogue[self.text_visualized][0] == "Fabiano":
                        self.image_visualized = 1
                    elif self.text_of_dialogue[self.text_visualized][0] == "Raul":
                        self.image_visualized = 2
                    else:
                        self.image_visualized = 0
                    
                    if self.text_visualized == 14:
                        self.background_visualized = 1
                        self.show_gui = False
                    elif self.text_visualized == 24:
                        self.background_visualized = 2
                        self.show_gui = False
                    else:
                        self.background_visualized = 0
                        self.show_gui = True
                        
            if input == "backspace":
                self.text_visualized = 0
                return True
                    
            if self.text_visualized == len(self.text_of_dialogue)-1:
                self.text_visualized = 0
                return True
        


d = Dialogues()