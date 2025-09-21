# Integração e Uso de Scripts Dinâmicos no WorkAdventure

Este guia explica como ativar scripts dinâmicos no seu mapa do WorkAdventure, usando o arquivo `public/mapScript.js` em conjunto com o mapa `public/wa_map-interativo.tmj`.

## 1. Conceito de map-scripting

O WorkAdventure permite adicionar “inteligência” ao mapa via JavaScript. O código roda no navegador do usuário e interage com o ambiente usando o objeto global `WA` (chat, camadas, pop-ups, websites, etc.).

## 2. Organização dos arquivos

- Mapa (TMJ): `public/wa_map-interativo.tmj`
- Script do mapa: `public/mapScript.js`
- No TMJ, a propriedade raiz `script` aponta para `mapScript.js` (caminho relativo ao TMJ).

Exemplo da propriedade no TMJ (raiz do JSON):

```json
{
  "properties": [
    { "name": "script", "type": "string", "value": "mapScript.js" }
  ]
}
```

## 3. Exemplo de `public/mapScript.js`

```javascript
/// <reference types="@workadventure/iframe-api-typings" />

WA.onInit().then(() => {
  // Mensagem de boas-vindas
  WA.chat.sendChatMessage(
    'Bem-vindo ao Hub da AR Online! Explore nosso espaço interativo.',
    'AR Online Bot'
  );

  // Ajuste os nomes para corresponder exatamente aos do Tiled/TMJ
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
```

Boas práticas:
- Mantenha os nomes de camadas/objetos consistentes. Evite acentos/espaços se possível (ex.: `telao-tecnologico`). Se optar por acentos, use exatamente o mesmo texto no script.
- Envolva sua lógica em `WA.onInit().then(() => { ... })`.

## 4. Abrindo websites e iframes

- `WA.ui.openCoWebSite('URL')` abre um site em um iframe dentro do WA.
- Para páginas que precisam conversar com o WA, defina o objeto no Tiled com `openWebsiteAllowApi: true` e, dentro do site, importe a Iframe API do WA.

## 5. CORS e segurança

Se o script acessar recursos externos, o servidor de destino deve expor cabeçalhos CORS apropriados. Observe também as restrições de sandbox nos iframes.

## 6. Publicação e testes

- Desenvolvimento: `npm run start` → `http://localhost:5173/`
- Preview produção: `npm run build` e `npm run prod` → `http://localhost:4173/`
- GitHub Pages (direto): `https://lourealiza.github.io/wa-aronline-hub/wa_map-interativo.tmj`
- WorkAdventure (global): `https://play.workadventu.re/_/global/lourealiza.github.io/wa-aronline-hub/wa_map-interativo.tmj`

## 7. Checklist

- [ ] `public/wa_map-interativo.tmj` possui a propriedade `script: "mapScript.js"` no nível raiz.
- [ ] `public/mapScript.js` existe e usa `WA.onInit()`.
- [ ] Nomes de camadas/objetos no script correspondem aos do Tiled.
- [ ] Se usar co-website, configurar `openWebsiteAllowApi: true` e a Iframe API na página.
- [ ] Testar localmente e via GitHub Pages + link WA Global.

