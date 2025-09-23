# 🗺️ Plano Detalhado do Mapa AR Online

## 📋 **Visão Geral**

O mapa do WorkAdventure da AR Online foi projetado para ser um escritório virtual completo e funcional, com divisões claras por departamento e áreas de convivência.

## 🏢 **Estrutura do Escritório**

### **Área Central - Lobby/Recepção**
- **Coordenadas**: x=20..59, y=30..44 (largura 40, altura 15)
- **Cor**: Azul vibrante (tile 725)
- **Função**: Circulação principal e recepção
- **Elementos**: Mesas de recepção, plantas decorativas, área de espera

### **Ala Esquerda - Gestão & CEO**
- **Coordenadas**: x=4..18, y=26..48 (largura 15, altura 23)
- **Cor**: Cinza claro (tile 2)
- **Subdivisões**:
  - **CEO**: x=4..8, y=26..30 (5x5)
  - **RH**: x=9..13, y=26..30 (5x5)
  - **Projetos**: x=4..8, y=31..35 (5x5)
  - **Processos & IA**: x=9..13, y=31..35 (5x5)
  - **Financeiro**: x=4..8, y=36..40 (5x5)
  - **Vendas**: x=9..13, y=36..40 (5x5)

### **Ala Direita - Operações**
- **Coordenadas**: x=61..75, y=26..48 (largura 15, altura 23)
- **Cor**: Cinza claro (tile 3)
- **Subdivisões**:
  - **Marketing**: x=61..65, y=26..30 (5x5)
  - **Comercial**: x=66..70, y=26..30 (5x5)
  - **Desenvolvimento**: x=61..65, y=31..35 (5x5)
  - **QA**: x=66..70, y=31..35 (5x5)
  - **DevOps**: x=61..65, y=36..40 (5x5)
  - **Suporte**: x=66..70, y=36..40 (5x5)

### **Parte Superior - Convivência & Eventos**
- **Coordenadas**: x=10..70, y=6..22 (largura 61, altura 17)
- **Cor**: Verde suave (tile 4)
- **Subdivisões**:
  - **Auditório**: x=10..25, y=6..12 (16x7)
  - **Jardim Virtual**: x=26..40, y=6..12 (15x7)
  - **Lounge/Copa**: x=41..55, y=6..12 (15x7)
  - **Treinamento**: x=56..70, y=6..12 (15x7)
  - **Sala de Reunião A**: x=10..16, y=13..18 (7x6)
  - **Sala de Reunião B**: x=18..24, y=13..18 (7x6)

## 🚶 **Sistema de Corredores**

### **Espinha Central**
- **Coordenadas**: x=39..40, y=22..52 (2 tiles de largura)
- **Função**: Conecta todas as áreas principais

### **Conectores**
- **Superior**: y=22..24, x=38..41 (Convivência ↔ Lobby)
- **Esquerdo**: y=26..27, x=19..20 (Lobby ↔ Gestão)
- **Direito**: y=26..27, x=59..60 (Lobby ↔ Operações)

## 🏗️ **Camadas do Mapa**

### **Camadas Estruturais**
1. **floor** - Piso base com cores por setor
2. **walls** - Paredes e divisórias
3. **collision** - Colisões (invisível)
4. **furniture** - Mobiliário e equipamentos
5. **decoration** - Plantas e decorações

### **Camadas Funcionais**
6. **start** - Ponto de spawn (centro do lobby)
7. **PrivateZones** - Zonas privadas por departamento
8. **zones** - Zonas especiais (Café, Impressão, etc.)

## 🎯 **Zonas Especiais**

### **Áreas de Convivência**
- **Café**: Espaço para conversas informais
- **Jardim Virtual**: Área relaxante com plantas
- **Lounge**: Espaço de descanso

### **Áreas de Trabalho**
- **Impressão**: Centro de impressão e documentos
- **Arquivo**: Documentação e arquivos
- **Auditório**: Eventos e apresentações

### **Salas de Reunião**
- **Sala A**: Reuniões pequenas (4-6 pessoas)
- **Sala B**: Reuniões médias (6-8 pessoas)
- **Auditório**: Eventos grandes (até 50 pessoas)

## 🎨 **Paleta de Cores**

| Setor | Cor | Tile ID | Descrição |
|-------|-----|---------|-----------|
| Lobby | Azul | 725 | Vibrante, acolhedor |
| Corredores | Cinza | 1 | Médio, neutro |
| Gestão | Cinza | 2 | Claro, profissional |
| Operações | Cinza | 3 | Claro, dinâmico |
| Convivência | Verde | 4 | Suave, relaxante |
| Paredes | - | 100 | Estruturais |
| Mobiliário | - | 200 | Funcional |
| Decoração | - | 300 | Estética |

## 🔧 **Elementos Interativos**

### **Hotspots por Sala**
- **CEO**: Agendamentos, reuniões executivas
- **RH**: Vagas, treinamentos, avaliações
- **Marketing**: Campanhas, métricas, eventos
- **Desenvolvimento**: Projetos, tecnologias, GitHub
- **QA**: Testes, bugs, documentação
- **Auditório**: Eventos, apresentações, equipamentos
- **Café**: Conversas, jogos, entretenimento
- **Impressão**: Documentos, relatórios, suporte
- **Arquivo**: Busca, contratos, histórico

### **Comandos de Chat**
- `/menu` - Menu principal
- `/integrations` - Status das integrações
- `/info` - Informações da empresa
- `/status` - Status da empresa
- `/team` - Informações da equipe
- `/projects` - Projetos ativos
- `/meeting` - Salas de reunião
- `/call [pessoa]` - Chamar membros da equipe

## 📊 **Métricas e Monitoramento**

### **Áreas de Tráfego**
- Lobby Central: Ponto de maior circulação
- Corredores: Fluxo entre departamentos
- Café: Área de convivência mais visitada

### **Zonas Privadas**
- CEO: Acesso restrito
- RH: Acesso controlado
- Desenvolvimento: Acesso técnico
- Marketing: Acesso criativo

## 🚀 **Funcionalidades Implementadas**

### **Navegação**
- ✅ Sistema de corredores
- ✅ Portas entre salas
- ✅ Ponto de spawn central
- ✅ Zonas de colisão

### **Interações**
- ✅ Mensagens por sala
- ✅ Comandos de chat
- ✅ Sistema de menu
- ✅ Informações departamentais

### **Integrações**
- ✅ Excalidraw (desenho colaborativo)
- ✅ Eraser (ferramenta de desenho)
- ✅ Cards (sistema Kanban)
- ❌ Google Docs/Drive (requer OAuth2)

## 📈 **Próximas Implementações**

### **Fase 1 - Melhorias Visuais**
- [ ] Adicionar mais mobiliário
- [ ] Implementar decorações específicas
- [ ] Criar hotspots visuais
- [ ] Adicionar NPCs informativos

### **Fase 2 - Funcionalidades Avançadas**
- [ ] Sistema de agendamento
- [ ] Chat privado por departamento
- [ ] Sistema de notificações
- [ ] Integração com calendário

### **Fase 3 - Gamificação**
- [ ] Sistema de conquistas
- [ ] Ranking de participação
- [ ] Eventos especiais
- [ ] Desafios departamentais

## 🔍 **Validação e Testes**

### **Testes de Navegação**
- [ ] Spawn no lobby central
- [ ] Acesso a todas as salas
- [ ] Colisões funcionando
- [ ] Portas acessíveis

### **Testes de Interação**
- [ ] Mensagens por sala
- [ ] Comandos de chat
- [ ] Menu principal
- [ ] Integrações básicas

### **Testes de Performance**
- [ ] Carregamento do mapa
- [ ] Responsividade
- [ ] Múltiplos usuários
- [ ] Estabilidade

## 📝 **Notas de Desenvolvimento**

- O mapa foi gerado automaticamente via script Python
- Todas as coordenadas são baseadas em tiles de 32x32 pixels
- As camadas seguem o padrão WorkAdventure
- O script de mapa está sincronizado com as camadas
- Documentação mantida atualizada com implementações
