/// <reference types="@workadventure/iframe-api-typings" />

WA.onInit().then(() => {
  // Mensagem de boas-vindas
  WA.chat.sendChatMessage(
    'Bem-vindo ao Hub da AR Online! Digite /menu para ver as opções disponíveis.',
    'AR Online Bot'
  );

  // Menu de construção e interações
  let buildMode = false;
  let selectedTool = null;

  // Comandos de chat
  WA.chat.onChatMessage((message) => {
    const text = message.text.toLowerCase();
    
    if (text === '/menu') {
      showMainMenu();
    } else if (text === '/build') {
      toggleBuildMode();
    } else if (text === '/help') {
      showHelp();
    } else if (text.startsWith('/tool ')) {
      const tool = text.split(' ')[1];
      selectTool(tool);
    } else if (text === '/clear') {
      clearMap();
    }
  });

  function showMainMenu() {
    WA.chat.sendChatMessage(
      '🏢 MENU PRINCIPAL - AR Online Hub\n' +
      '📋 Comandos disponíveis:\n' +
      '/build - Ativar/desativar modo construção\n' +
      '/tool [nome] - Selecionar ferramenta\n' +
      '/clear - Limpar mapa\n' +
      '/help - Ajuda detalhada\n' +
      '🎯 Ferramentas: wall, floor, furniture, decoration',
      'Sistema'
    );
  }

  function toggleBuildMode() {
    buildMode = !buildMode;
    WA.chat.sendChatMessage(
      `🔨 Modo construção: ${buildMode ? 'ATIVADO' : 'DESATIVADO'}`,
      'Sistema'
    );
    
    if (buildMode) {
      WA.chat.sendChatMessage(
        'Use /tool [wall/floor/furniture/decoration] para selecionar ferramenta',
        'Sistema'
      );
    }
  }

  function selectTool(tool) {
    if (!buildMode) {
      WA.chat.sendChatMessage('Ative o modo construção primeiro com /build', 'Sistema');
      return;
    }

    const tools = ['wall', 'floor', 'furniture', 'decoration'];
    if (tools.includes(tool)) {
      selectedTool = tool;
      WA.chat.sendChatMessage(`🔧 Ferramenta selecionada: ${tool}`, 'Sistema');
    } else {
      WA.chat.sendChatMessage('Ferramenta inválida. Use: wall, floor, furniture, decoration', 'Sistema');
    }
  }

  function showHelp() {
    WA.chat.sendChatMessage(
      '📖 AJUDA - Sistema de Construção\n' +
      '1. Digite /build para ativar o modo construção\n' +
      '2. Use /tool [nome] para selecionar ferramenta\n' +
      '3. Clique no mapa para colocar elementos\n' +
      '4. Use /clear para limpar tudo\n' +
      '5. Digite /menu para ver comandos\n\n' +
      '🎨 Ferramentas disponíveis:\n' +
      '• wall - Paredes e divisórias\n' +
      '• floor - Pisos e carpetes\n' +
      '• furniture - Mesas, cadeiras, equipamentos\n' +
      '• decoration - Plantas, quadros, decorações',
      'Sistema'
    );
  }

  function clearMap() {
    WA.chat.sendChatMessage('🧹 Limpando mapa...', 'Sistema');
    // Aqui você pode implementar a lógica para limpar o mapa
    WA.chat.sendChatMessage('Mapa limpo! Use /build para começar a construir.', 'Sistema');
  }

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

  WA.room.onEnterLayer('Balcão Atendimento').subscribe(() => {
    WA.chat.sendChatMessage(
      'Bem-vindo ao balcão de atendimento! Como posso ajudá-lo hoje?',
      'AR Online Bot'
    );
    // WA.ui.openCoWebSite('https://aria.ar-online.com');
  });

  // Interações por tipo de sala
  WA.room.onEnterLayer('Desenvolvimento').subscribe(() => {
    WA.chat.sendChatMessage(
      'Área de Desenvolvimento - Equipe de programação e desenvolvimento de software.',
      'Sistema'
    );
  });

  WA.room.onEnterLayer('QA').subscribe(() => {
    WA.chat.sendChatMessage(
      'Área de QA - Testes e garantia de qualidade dos produtos.',
      'Sistema'
    );
  });

  WA.room.onEnterLayer('DevOps').subscribe(() => {
    WA.chat.sendChatMessage(
      'Área de DevOps - Infraestrutura e deploy automatizado.',
      'Sistema'
    );
  });

  WA.room.onEnterLayer('Marketing').subscribe(() => {
    WA.chat.sendChatMessage(
      'Área de Marketing - Campanhas e estratégias de marketing digital.',
      'Sistema'
    );
  });

  WA.room.onEnterLayer('Design').subscribe(() => {
    WA.chat.sendChatMessage(
      'Área de Design - Criação visual e experiência do usuário.',
      'Sistema'
    );
  });

  WA.room.onEnterLayer('RH').subscribe(() => {
    WA.chat.sendChatMessage(
      'Recursos Humanos - Gestão de pessoas e processos internos.',
      'Sistema'
    );
  });

  WA.room.onEnterLayer('Financeiro').subscribe(() => {
    WA.chat.sendChatMessage(
      'Área Financeira - Controle financeiro e planejamento orçamentário.',
      'Sistema'
    );
  });

  WA.room.onEnterLayer('Vendas').subscribe(() => {
    WA.chat.sendChatMessage(
      'Área de Vendas - Estratégias comerciais e relacionamento com clientes.',
      'Sistema'
    );
  });

  WA.room.onEnterLayer('Suporte').subscribe(() => {
    WA.chat.sendChatMessage(
      'Área de Suporte - Atendimento ao cliente e suporte técnico.',
      'Sistema'
    );
  });

  // Salas de reunião
  WA.room.onEnterLayer('Sala de Reunião A').subscribe(() => {
    WA.chat.sendChatMessage(
      'Sala de Reunião A - Disponível para reuniões da equipe.',
      'Sistema'
    );
  });

  WA.room.onEnterLayer('Sala de Reunião B').subscribe(() => {
    WA.chat.sendChatMessage(
      'Sala de Reunião B - Disponível para reuniões da equipe.',
      'Sistema'
    );
  });

  WA.room.onEnterLayer('Auditório').subscribe(() => {
    WA.chat.sendChatMessage(
      'Auditório - Espaço para apresentações e eventos corporativos.',
      'Sistema'
    );
  });

  WA.room.onEnterLayer('Treinamento').subscribe(() => {
    WA.chat.sendChatMessage(
      'Sala de Treinamento - Capacitação e desenvolvimento da equipe.',
      'Sistema'
    );
  });

  // Zona privada da diretoria
  WA.room.onEnterLayer('Diretoria_Private_Zone').subscribe(() => {
    WA.chat.sendChatMessage(
      'Zona Privada - Acesso restrito à diretoria.',
      'Sistema'
    );
  });

  // NPC RH: menu simples via chat
  // Comentado - camadas não existem no novo mapa
  /*
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
  // Porta com senha (demo): abre removendo colisões no "vão" (3 tiles)
  // Coordenadas (tiles) do vão calculadas a partir do layout atual (W=70,H=50)
  const DOOR = { layer: 'porta-1', tiles: [ {x:34,y:17}, {x:35,y:17}, {x:36,y:17} ], password: 'AR2025' };
  WA.room.onEnterLayer(DOOR.layer).subscribe(async () => {
    const ans = prompt('Senha da porta:');
    if (ans === DOOR.password) {
      try {
        for (const t of DOOR.tiles) {
          await WA.room.setTile(t.x, t.y, 0);
        }
        WA.chat.sendChatMessage('Porta destrancada.', 'Sistema');
      } catch (e) { console.warn(e); }
    } else {
      WA.chat.sendChatMessage('Senha incorreta.', 'Sistema');
    }
  });
  */
  // Handlers para nomes normalizados (sem acentos) - Comentado pois já temos os handlers acima
  /*
  WA.room.onEnterLayer('ar-online-logo').subscribe(() => {
    WA.chat.sendChatMessage(
      'Olá! Este é o logo da AR Online. Clique para saber mais.',
      'AR Online Bot'
    );
    // WA.ui.openCoWebSite('https://www.ar-online.com.br/sobre');
  });
  WA.room.onEnterLayer('telao-tecnologico').subscribe(() => {
    WA.chat.sendChatMessage(
      'Assista aos nossos vídeos institucionais ou confira os dashboards!',
      'AR Online Bot'
    );
    // WA.ui.openCoWebSite('https://www.ar-online.com.br/video-institucional');
  });
  */
});
