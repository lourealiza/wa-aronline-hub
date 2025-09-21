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
});

