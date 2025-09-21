/// <reference types="@workadventure/iframe-api-typings" />

WA.onInit().then(() => {
  // Mensagem de boas-vindas
  WA.chat.sendChatMessage(
    'Bem-vindo ao Hub da AR Online! Explore nosso espaço interativo.',
    'AR Online Bot'
  );

  // Exemplos de interações por nome de camada/objeto no Tiled
  // Ajuste os nomes abaixo para corresponder exatamente aos nomes no TMJ/Tiled
  WA.room.onEnterLayer('AR Online Logo').subscribe(() => {
    WA.chat.sendChatMessage(
      'Olá! Este é o logo da AR Online. Clique para saber mais.',
      'AR Online Bot'
    );
    // WA.ui.openCoWebSite('https://www.ar-online.com.br/sobre');
  });

  WA.room.onEnterLayer('Telão Tecnológico').subscribe(() => {
    WA.chat.sendChatMessage(
      'Assista aos nossos vídeos institucionais ou confira os dashboards!',
      'AR Online Bot'
    );
    // WA.ui.openCoWebSite('https://www.ar-online.com.br/video-institucional');
  });

  // NPC RH: menu simples via chat
  let awaitingNpc = null;
  const openIf = (fn) => { try { fn && fn(); } catch (e) { console.warn(e); } };

  WA.room.onEnterLayer('npc-rh').subscribe(() => {
    awaitingNpc = 'rh';
    WA.chat.sendChatMessage('RH: Digite uma opção: beneficios | vagas | treinamentos', 'NPC RH');
  });
  WA.room.onLeaveLayer('npc-rh').subscribe(() => { if (awaitingNpc === 'rh') awaitingNpc = null; });

  if (WA.chat && typeof WA.chat.onChatMessage === 'function') {
    WA.chat.onChatMessage((msg) => {
      if (!awaitingNpc) return;
      const text = (msg?.text || '').toLowerCase();
      if (awaitingNpc === 'rh') {
        if (text.includes('benef')) {
          openIf(() => WA.ui.openCoWebSite('https://rh.ar-online.com/beneficios'));
        } else if (text.includes('vaga')) {
          openIf(() => WA.ui.openCoWebSite('https://rh.ar-online.com/vagas'));
        } else if (text.includes('trein')) {
          openIf(() => WA.ui.openCoWebSite('https://rh.ar-online.com/treinamentos'));
        } else {
          WA.chat.sendChatMessage('Opções: beneficios | vagas | treinamentos', 'NPC RH');
          return;
        }
        awaitingNpc = null;
      }
    });
  }

  // NPC Guia: abre guia rápido (página de navegação)
  WA.room.onEnterLayer('npc-guia').subscribe(() => {
    openIf(() => WA.ui.openCoWebSite('/widgets/guia.html'));
  });

  // Widgets: feed, countdown, mural, enquete, quiz/minigame
  WA.room.onEnterLayer('feed-noticias').subscribe(() => {
    openIf(() => WA.ui.openCoWebSite('/widgets/feed.html'));
  });
  WA.room.onEnterLayer('countdown-evento').subscribe(() => {
    // Ajuste a data via querystring se quiser (ex.: ?date=2025-12-31T23:59:59)
    openIf(() => WA.ui.openCoWebSite('/widgets/countdown.html'));
  });
  WA.room.onEnterLayer('mural-colaboracao').subscribe(() => {
    openIf(() => WA.ui.openCoWebSite('/widgets/mural.html'));
  });
  WA.room.onEnterLayer('votacao-enquete').subscribe(() => {
    openIf(() => WA.ui.openCoWebSite('/widgets/poll.html'));
  });
  WA.room.onEnterLayer('minigame-quiz').subscribe(() => {
    openIf(() => WA.ui.openCoWebSite('/widgets/quiz.html'));
  });
});
