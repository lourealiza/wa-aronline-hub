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

  // Comandos de chat - Sistema simplificado para WorkAdventure
  WA.chat.onChatMessage((message) => {
    const text = message.text.toLowerCase();
    
    if (text === '/menu' || text === '/help') {
      showMainMenu();
    } else if (text === '/status') {
      showCompanyStatus();
    } else if (text === '/team') {
      showTeamInfo();
    } else if (text === '/projects') {
      showActiveProjects();
    } else if (text === '/meeting') {
      showMeetingRooms();
    } else if (text.startsWith('/call ')) {
      const person = text.split(' ')[1];
      callPerson(person);
    } else if (text === '/weather') {
      showWeather();
    } else if (text === '/news') {
      showCompanyNews();
    } else if (text === '/info') {
      showCompanyInfo();
    } else if (text === '/integrations') {
      showIntegrationsInfo();
    }
  });

  function showMainMenu() {
    WA.chat.sendChatMessage(
      '🏢 MENU PRINCIPAL - AR Online Hub\n' +
      '📊 COMANDOS DE INFORMAÇÃO:\n' +
      '/status - Status da empresa\n' +
      '/team - Informações da equipe\n' +
      '/projects - Projetos ativos\n' +
      '/meeting - Salas de reunião\n' +
      '/news - Notícias da empresa\n' +
      '/weather - Clima atual\n' +
      '/info - Informações da AR Online\n' +
      '/integrations - Status das integrações\n\n' +
      '📞 COMANDOS DE COMUNICAÇÃO:\n' +
      '/call [pessoa] - Chamar alguém\n' +
      'Pessoas: lou, milena, caroline, dev, marketing\n\n' +
      '🔨 CONSTRUÇÃO:\n' +
      'Use o menu "Mapa" → "Editor de mapa" para construir\n' +
      'Navegue pelas salas para ver informações específicas',
      'Sistema'
    );
  }

  function showCompanyInfo() {
    WA.chat.sendChatMessage(
      '🏢 AR ONLINE - Informações da Empresa\n' +
      '📍 Localização: São Paulo, SP\n' +
      '🎯 Missão: Transformar comunicação empresarial\n' +
      '💼 Serviços: AR-Email, AR-SMS, AR-WhatsApp, AR-Voz\n' +
      '🤖 Produto principal: ARIA (Chatbot inteligente)\n' +
      '📈 Fundada em: 2020\n' +
      '👥 Equipe: 25+ profissionais\n' +
      '🌐 Site: www.ar-online.com.br\n\n' +
      '🔗 INTEGRAÇÕES DISPONÍVEIS:\n' +
      '📄 Google Docs - Documentos colaborativos\n' +
      '💾 Google Drive - Compartilhamento de arquivos\n' +
      '🎨 Excalidraw - Desenho colaborativo\n' +
      '💡 Para habilitar: Configure OAuth2 no servidor',
      'Sistema Info'
    );
  }

  function showIntegrationsInfo() {
    WA.chat.sendChatMessage(
      '🔗 INTEGRAÇÕES WORKADVENTURE - AR Online\n\n' +
      '📄 GOOGLE DOCS:\n' +
      '• Status: Desabilitada (requer configuração OAuth2)\n' +
      '• Uso: Documentos colaborativos em tempo real\n' +
      '• Configuração: Servidor + credenciais Google\n\n' +
      '💾 GOOGLE DRIVE:\n' +
      '• Status: Desabilitada (requer configuração OAuth2)\n' +
      '• Uso: Compartilhamento de arquivos\n' +
      '• Configuração: Servidor + credenciais Google\n\n' +
      '🎨 EXCALIDRAW:\n' +
      '• Status: Desabilitada (requer servidor)\n' +
      '• Uso: Desenho colaborativo e brainstorming\n' +
      '• Configuração: Backend + banco de dados\n\n' +
      '🧹 BORRACHA (ERASER):\n' +
      '• Status: Desabilitada (requer servidor)\n' +
      '• Uso: Desenho colaborativo\n' +
      '• Configuração: Servidor de desenho\n\n' +
      '📋 CARDS:\n' +
      '• Status: Desabilitada (requer banco de dados)\n' +
      '• Uso: Sistema Kanban colaborativo\n' +
      '• Configuração: Banco de dados + servidor\n\n' +
      '💡 Para habilitar integrações, configure um servidor WorkAdventure completo.',
      'Sistema Integrações'
    );
  }

  // Sistema de construção removido - usar Editor de Mapa do WorkAdventure

  // ===== SISTEMA DE NOTIFICAÇÕES E COMANDOS AVANÇADOS =====
  
  // Comandos adicionais
  WA.chat.onChatMessage((message) => {
    const text = message.text.toLowerCase();
    
    if (text === '/status') {
      showCompanyStatus();
    } else if (text === '/team') {
      showTeamInfo();
    } else if (text === '/projects') {
      showActiveProjects();
    } else if (text === '/meeting') {
      showMeetingRooms();
    } else if (text.startsWith('/call ')) {
      const person = text.split(' ')[1];
      callPerson(person);
    } else if (text === '/weather') {
      showWeather();
    } else if (text === '/news') {
      showCompanyNews();
    }
  });

  function showCompanyStatus() {
    WA.chat.sendChatMessage(
      '📊 STATUS DA EMPRESA - AR Online\n' +
      '🟢 Sistema: Online\n' +
      '👥 Funcionários: 25 conectados\n' +
      '💼 Projetos ativos: 8\n' +
      '🎯 Metas do mês: 85% atingidas\n' +
      '📈 Crescimento: +15% este trimestre',
      'Sistema Status'
    );
  }

  function showTeamInfo() {
    WA.chat.sendChatMessage(
      '👥 EQUIPE AR ONLINE\n' +
      '💻 Desenvolvimento: 8 pessoas\n' +
      '🎨 Design: 3 pessoas\n' +
      '📈 Marketing: 4 pessoas\n' +
      '💼 Vendas: 5 pessoas\n' +
      '🎧 Suporte: 3 pessoas\n' +
      '👥 RH: 2 pessoas',
      'Sistema Equipe'
    );
  }

  function showActiveProjects() {
    WA.chat.sendChatMessage(
      '📋 PROJETOS ATIVOS\n' +
      '🤖 ARIA: Chatbot inteligente - 90%\n' +
      '🔗 Integrações: APIs externas - 75%\n' +
      '📱 App Mobile: Nova versão - 60%\n' +
      '☁️ Migração Cloud: Infraestrutura - 40%\n' +
      '🎯 CRM: Atualização sistema - 85%',
      'Sistema Projetos'
    );
  }

  function showMeetingRooms() {
    WA.chat.sendChatMessage(
      '🏢 SALAS DE REUNIÃO\n' +
      '📅 Sala A: Disponível (8 pessoas)\n' +
      '📅 Sala B: Disponível (6 pessoas)\n' +
      '🎭 Auditório: Disponível (50 pessoas)\n' +
      '🎓 Treinamento: Disponível (20 pessoas)\n' +
      '💡 Dica: Use /meeting [sala] para reservar',
      'Sistema Reuniões'
    );
  }

  function callPerson(person) {
    const people = {
      'lou': 'Lou - Desenvolvedor Principal',
      'milena': 'Milena - Gestão de Projetos',
      'caroline': 'Caroline - RH',
      'dev': 'Equipe de Desenvolvimento',
      'marketing': 'Equipe de Marketing'
    };
    
    const personInfo = people[person.toLowerCase()];
    if (personInfo) {
      WA.chat.sendChatMessage(
        `📞 Chamando ${personInfo}...\n` +
        '🔔 Notificação enviada!\n' +
        '⏰ Aguardando resposta...',
        'Sistema Chamadas'
      );
    } else {
      WA.chat.sendChatMessage(
        'Pessoa não encontrada. Use: lou, milena, caroline, dev, marketing',
        'Sistema Chamadas'
      );
    }
  }

  function showWeather() {
    WA.chat.sendChatMessage(
      '🌤️ CLIMA ATUAL\n' +
      '📍 São Paulo, SP\n' +
      '🌡️ Temperatura: 24°C\n' +
      '☁️ Condição: Parcialmente nublado\n' +
      '💨 Vento: 12 km/h\n' +
      '🌧️ Chuva: 20% de chance',
      'Sistema Clima'
    );
  }

  function showCompanyNews() {
    WA.chat.sendChatMessage(
      '📰 NOTÍCIAS DA EMPRESA\n' +
      '🎉 Nova contratação na área de Marketing\n' +
      '📈 Crescimento de 15% nas vendas\n' +
      '🏆 Prêmio de melhor atendimento\n' +
      '🚀 Lançamento do ARIA 2.0\n' +
      '💼 Parceria com nova empresa',
      'Sistema Notícias'
    );
  }

  // ===== SISTEMA DE ACHIEVEMENTS E GAMIFICAÇÃO =====
  
  let achievements = {
    explorer: false,
    social: false,
    builder: false,
    meeting: false
  };

  // Achievement: Explorador
  let visitedRooms = new Set();
  WA.room.onEnterLayer('*').subscribe((layerName) => {
    visitedRooms.add(layerName);
    if (visitedRooms.size >= 5 && !achievements.explorer) {
      achievements.explorer = true;
      WA.chat.sendChatMessage(
        '🏆 CONQUISTA DESBLOQUEADA!\n' +
        '🌟 Explorador: Visitei 5 salas diferentes\n' +
        '🎁 Recompensa: Acesso a área VIP',
        'Sistema Conquistas'
      );
    }
  });

  // Achievement: Construtor
  let buildCount = 0;
  WA.chat.onChatMessage((message) => {
    if (message.text.toLowerCase().startsWith('/tool ')) {
      buildCount++;
      if (buildCount >= 3 && !achievements.builder) {
        achievements.builder = true;
        WA.chat.sendChatMessage(
          '🏆 CONQUISTA DESBLOQUEADA!\n' +
          '🔨 Construtor: Usei 3 ferramentas diferentes\n' +
          '🎁 Recompensa: Ferramentas premium',
          'Sistema Conquistas'
        );
      }
    }
  });

  // ===== INTERAÇÕES POR SETOR =====
  
  // LOBBY CENTRAL - Recepção e informações gerais
  WA.room.onEnterLayer('Lobby Central').subscribe(() => {
    WA.chat.sendChatMessage(
      '🏢 Bem-vindo ao Lobby Central da AR Online!\n' +
      '📍 Área Central - Circulação principal\n' +
      '🎯 Acesso a todos os setores da empresa\n' +
      '💡 Digite /menu para ver comandos disponíveis\n' +
      '🚶 Navegue pelos corredores para acessar outras áreas\n' +
      '🎪 Eventos e reuniões acontecem aqui!',
      'Recepção AR Online'
    );
  });

  // GESTÃO & CEO - Área administrativa
  WA.room.onEnterLayer('Gestão & CEO').subscribe(() => {
    WA.chat.sendChatMessage(
      '👔 Área de Gestão & CEO\n' +
      '🏢 CEO, Projetos, RH, Processos/Inovação\n' +
      '📊 Gestão estratégica e administrativa\n' +
      '💼 Decisões executivas e planejamento\n' +
      '🎯 Subdivisões serão implementadas em breve',
      'Sistema Gestão'
    );
  });

  // OPERAÇÕES - Área operacional
  WA.room.onEnterLayer('Operações').subscribe(() => {
    WA.chat.sendChatMessage(
      '⚙️ Área de Operações\n' +
      '💼 Comercial (4 salas), Marketing, Devs, Suporte\n' +
      '🚀 Execução de projetos e atendimento\n' +
      '📈 Operações comerciais e técnicas\n' +
      '🎯 Subdivisões serão implementadas em breve',
      'Sistema Operações'
    );
  });

  // CONVIVÊNCIA & EVENTOS - Área de relaxamento
  WA.room.onEnterLayer('Convivência & Eventos').subscribe(() => {
    WA.chat.sendChatMessage(
      '🌿 Área de Convivência & Eventos\n' +
      '🎭 Auditório, Jardim Virtual, Lounge/Copa\n' +
      '☕ Espaço para relaxamento e eventos\n' +
      '🎉 Celebrações e treinamentos\n' +
      '🎯 Subdivisões serão implementadas em breve',
      'Sistema Convivência'
    );
  });

  // CORREDORES - Áreas de circulação
  WA.room.onEnterLayer('Espinha Central').subscribe(() => {
    WA.chat.sendChatMessage(
      '🚶 Corredor Principal - Espinha Central\n' +
      '↕️ Conecta Convivência ↔ Lobby ↔ Alas\n' +
      '📍 Navegação principal do escritório',
      'Sistema Navegação'
    );
  });

  WA.room.onEnterLayer('Conector Superior').subscribe(() => {
    WA.chat.sendChatMessage(
      '🔗 Conector Superior\n' +
      '↕️ Liga Convivência ↔ Lobby\n' +
      '📍 Acesso à área de eventos',
      'Sistema Navegação'
    );
  });

  WA.room.onEnterLayer('Conector Esquerdo').subscribe(() => {
    WA.chat.sendChatMessage(
      '🔗 Conector Esquerdo\n' +
      '↔️ Liga Lobby ↔ Gestão & CEO\n' +
      '📍 Acesso à área administrativa',
      'Sistema Navegação'
    );
  });

  WA.room.onEnterLayer('Conector Direito').subscribe(() => {
    WA.chat.sendChatMessage(
      '🔗 Conector Direito\n' +
      '↔️ Liga Lobby ↔ Operações\n' +
      '📍 Acesso à área operacional',
      'Sistema Navegação'
    );
  });

  // DESENVOLVIMENTO - Equipe de programação
  WA.room.onEnterLayer('Desenvolvimento').subscribe(() => {
    WA.chat.sendChatMessage(
      '💻 Área de Desenvolvimento - Equipe de Programação\n' +
      '🔧 Ferramentas: GitHub, Bitbucket, VS Code\n' +
      '📋 Projetos ativos: ARIA, Integrações, Automações\n' +
      '👥 Equipe: Desenvolvedores Full-Stack',
      'Sistema Dev'
    );
    
    // Abrir link para GitHub se disponível
    try {
      WA.ui.openCoWebSite('https://github.com/lourealiza');
    } catch (e) {
      console.log('GitHub link não disponível');
    }
  });

  // QA & DEVOPS - Testes e infraestrutura
  WA.room.onEnterLayer('QA').subscribe(() => {
    WA.chat.sendChatMessage(
      '🧪 Área de QA - Testes e Garantia de Qualidade\n' +
      '🔍 Testes automatizados e manuais\n' +
      '📊 Relatórios de bugs e performance\n' +
      '✅ Validação de funcionalidades',
      'Sistema QA'
    );
  });

  WA.room.onEnterLayer('DevOps').subscribe(() => {
    WA.chat.sendChatMessage(
      '⚙️ Área de DevOps - Infraestrutura e Deploy\n' +
      '🚀 CI/CD automatizado\n' +
      '☁️ Gerenciamento de servidores\n' +
      '📈 Monitoramento e logs',
      'Sistema DevOps'
    );
  });

  // MARKETING & DESIGN - Campanhas e criação visual
  WA.room.onEnterLayer('Marketing').subscribe(() => {
    WA.chat.sendChatMessage(
      '📈 Área de Marketing - Campanhas Digitais\n' +
      '🎯 Google Ads, Facebook Ads\n' +
      '📱 Redes sociais e conteúdo\n' +
      '📊 Analytics e métricas',
      'Sistema Marketing'
    );
    
    try {
      WA.ui.openCoWebSite('https://ads.google.com');
    } catch (e) {
      console.log('Google Ads link não disponível');
    }
  });

  WA.room.onEnterLayer('Design').subscribe(() => {
    WA.chat.sendChatMessage(
      '🎨 Área de Design - Criação Visual\n' +
      '🖼️ Identidade visual da AR Online\n' +
      '📐 Protótipos e wireframes\n' +
      '🎭 Materiais de marketing',
      'Sistema Design'
    );
  });

  // RH & FINANCEIRO - Gestão de pessoas e recursos
  WA.room.onEnterLayer('RH').subscribe(() => {
    WA.chat.sendChatMessage(
      '👥 Área de RH - Recursos Humanos\n' +
      '📋 Recrutamento e seleção\n' +
      '🎓 Treinamentos e desenvolvimento\n' +
      '💼 Políticas e benefícios',
      'Sistema RH'
    );
  });

  WA.room.onEnterLayer('Financeiro').subscribe(() => {
    WA.chat.sendChatMessage(
      '💰 Área Financeira - Controle Financeiro\n' +
      '📊 Relatórios e análises\n' +
      '💳 Contas a pagar e receber\n' +
      '📈 Planejamento orçamentário',
      'Sistema Financeiro'
    );
  });

  // VENDAS & SUPORTE - Comercial e atendimento
  WA.room.onEnterLayer('Vendas').subscribe(() => {
    WA.chat.sendChatMessage(
      '💼 Área de Vendas - Estratégias Comerciais\n' +
      '🎯 CRM Vtiger\n' +
      '📞 Prospecção e follow-up\n' +
      '📈 Metas e resultados',
      'Sistema Vendas'
    );
    
    try {
      WA.ui.openCoWebSite('https://vtiger.com');
    } catch (e) {
      console.log('Vtiger link não disponível');
    }
  });

  WA.room.onEnterLayer('Suporte').subscribe(() => {
    WA.chat.sendChatMessage(
      '🎧 Área de Suporte - Atendimento ao Cliente\n' +
      '🎫 Sistema de tickets\n' +
      '📞 Suporte técnico\n' +
      '⏱️ SLAs e métricas',
      'Sistema Suporte'
    );
    
    try {
      WA.ui.openCoWebSite('https://zendesk.com');
    } catch (e) {
      console.log('Zendesk link não disponível');
    }
  });

  // SALAS DE REUNIÃO
  WA.room.onEnterLayer('Sala de Reunião A').subscribe(() => {
    WA.chat.sendChatMessage(
      '🏢 Sala de Reunião A - Disponível para reuniões\n' +
      '📅 Capacidade: 8 pessoas\n' +
      '🖥️ Equipamentos: Projetor, TV\n' +
      '☕ Serviços: Café e água',
      'Sistema Reuniões'
    );
  });

  WA.room.onEnterLayer('Sala de Reunião B').subscribe(() => {
    WA.chat.sendChatMessage(
      '🏢 Sala de Reunião B - Disponível para reuniões\n' +
      '📅 Capacidade: 6 pessoas\n' +
      '🖥️ Equipamentos: TV, quadro branco\n' +
      '☕ Serviços: Café e água',
      'Sistema Reuniões'
    );
  });

  // AUDITÓRIO E TREINAMENTO
  WA.room.onEnterLayer('Auditório').subscribe(() => {
    WA.chat.sendChatMessage(
      '🎭 Auditório - Eventos e Apresentações\n' +
      '👥 Capacidade: 50 pessoas\n' +
      '🎤 Equipamentos: Microfone, projetor\n' +
      '📺 Streaming disponível',
      'Sistema Eventos'
    );
  });

  WA.room.onEnterLayer('Treinamento').subscribe(() => {
    WA.chat.sendChatMessage(
      '🎓 Sala de Treinamento - Capacitação da Equipe\n' +
      '👥 Capacidade: 20 pessoas\n' +
      '💻 Computadores disponíveis\n' +
      '📚 Material didático',
      'Sistema Treinamento'
    );
  });

  // ===== ZONAS ESPECIAIS E INTERAÇÕES =====
  
  // Zona de café/pausa
  WA.room.onEnterLayer('Café').subscribe(() => {
    WA.chat.sendChatMessage(
      '☕ Área de Café - Pausa para relaxar\n' +
      '🍰 Lanches e bebidas disponíveis\n' +
      '💬 Espaço para conversas informais\n' +
      '🎮 Jogos e entretenimento',
      'Sistema Café'
    );
  });

  // Zona de impressão/copiadora
  WA.room.onEnterLayer('Impressão').subscribe(() => {
    WA.chat.sendChatMessage(
      '🖨️ Área de Impressão - Documentos e cópias\n' +
      '📄 Impressoras disponíveis\n' +
      '📋 Papel e suprimentos\n' +
      '🔧 Suporte técnico',
      'Sistema Impressão'
    );
  });

  // Zona de arquivo/armazenamento
  WA.room.onEnterLayer('Arquivo').subscribe(() => {
    WA.chat.sendChatMessage(
      '📁 Área de Arquivo - Documentos e armazenamento\n' +
      '🗂️ Organização de documentos\n' +
      '🔒 Acesso controlado\n' +
      '📋 Inventário atualizado',
      'Sistema Arquivo'
    );
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
  // ===== INTERAÇÕES DETALHADAS POR SALA =====
  
  // CEO - Gabinete executivo
  WA.room.onEnterLayer('CEO').subscribe(() => {
    WA.chat.sendChatMessage(
      '👑 Gabinete do CEO - Louisa Realiza\n' +
      '🎯 Decisões estratégicas e visão da empresa\n' +
      '📈 Crescimento e expansão da AR Online\n' +
      '🤝 Reuniões executivas e planejamento\n' +
      '💼 Agendamentos: contato@ar-online.com.br',
      'Sistema CEO'
    );
  });

  // RH - Recursos Humanos
  WA.room.onEnterLayer('RH').subscribe(() => {
    WA.chat.sendChatMessage(
      '👥 Recursos Humanos - Caroline\n' +
      '📋 Gestão de pessoas e cultura organizacional\n' +
      '🎓 Treinamentos e desenvolvimento\n' +
      '📊 Avaliações e feedback\n' +
      '💼 Vagas abertas: rh@ar-online.com.br',
      'Sistema RH'
    );
  });

  // MARKETING - Estratégia de mercado
  WA.room.onEnterLayer('Marketing').subscribe(() => {
    WA.chat.sendChatMessage(
      '📢 Área de Marketing - Milena\n' +
      '🎯 Estratégias de mercado e branding\n' +
      '📱 Redes sociais e conteúdo digital\n' +
      '📊 Campanhas e métricas de performance\n' +
      '🚀 Lançamentos e eventos da empresa',
      'Sistema Marketing'
    );
  });

  // QA - Qualidade e Testes
  WA.room.onEnterLayer('QA').subscribe(() => {
    WA.chat.sendChatMessage(
      '🔍 Área de QA - Qualidade e Testes\n' +
      '✅ Garantia de qualidade dos produtos\n' +
      '🧪 Testes automatizados e manuais\n' +
      '🐛 Relatórios de bugs e correções\n' +
      '📋 Documentação técnica e processos',
      'Sistema QA'
    );
  });

  // AUDITÓRIO - Eventos e apresentações
  WA.room.onEnterLayer('Auditório').subscribe(() => {
    WA.chat.sendChatMessage(
      '🎭 Auditório - Eventos e Apresentações\n' +
      '📺 Capacidade: 50 pessoas\n' +
      '🎤 Apresentações e treinamentos\n' +
      '📅 Próximo evento: Reunião Geral (Sexta 15h)\n' +
      '💡 Equipamentos: Projetor, Som, Wi-Fi',
      'Sistema Auditório'
    );
  });

  // CAFÉ - Área de convivência
  WA.room.onEnterLayer('Café').subscribe(() => {
    WA.chat.sendChatMessage(
      '☕ Café - Área de Convivência\n' +
      '🍵 Café, chá e lanches disponíveis\n' +
      '💬 Espaço para conversas informais\n' +
      '🎮 Jogos e entretenimento\n' +
      '🌱 Plantas e ambiente relaxante',
      'Sistema Café'
    );
  });

  // IMPRESSÃO - Centro de impressão
  WA.room.onEnterLayer('Impressão').subscribe(() => {
    WA.chat.sendChatMessage(
      '🖨️ Centro de Impressão\n' +
      '📄 Impressoras coloridas e P&B\n' +
      '📋 Documentos corporativos\n' +
      '📊 Relatórios e apresentações\n' +
      '💡 Suporte técnico disponível',
      'Sistema Impressão'
    );
  });

  // ARQUIVO - Documentação
  WA.room.onEnterLayer('Arquivo').subscribe(() => {
    WA.chat.sendChatMessage(
      '📁 Arquivo - Documentação\n' +
      '📚 Documentos históricos da empresa\n' +
      '📋 Contratos e acordos\n' +
      '📊 Relatórios e análises\n' +
      '🔍 Sistema de busca digital',
      'Sistema Arquivo'
    );
  });

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
