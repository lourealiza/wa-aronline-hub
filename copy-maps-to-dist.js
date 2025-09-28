#!/usr/bin/env node
/**
 * Script para copiar arquivos de mapa para a pasta dist após o build
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Arquivos de mapa para copiar
const mapFiles = [
  'wa_map-interativo.tmj',
  'wa_map-ar-online-professional.tmj',
  'wa_map-working.tmj',
  'wa_map-complexo.tmj'
];

const additionalFiles = [
  'editor.html',
  'ar-online-objects.json'
];

// Função para copiar arquivo
function copyFile(source, dest) {
  try {
    if (fs.existsSync(source)) {
      fs.copyFileSync(source, dest);
      console.log(`✅ Copiado: ${source} -> ${dest}`);
    } else {
      console.log(`❌ Arquivo não encontrado: ${source}`);
    }
  } catch (error) {
    console.error(`❌ Erro ao copiar ${source}:`, error.message);
  }
}

// Criar pasta dist se não existir
if (!fs.existsSync('dist')) {
  fs.mkdirSync('dist', { recursive: true });
}

// Copiar arquivos de mapa
console.log('📁 Copiando arquivos de mapa para dist/...');
mapFiles.forEach(file => {
  copyFile(file, `dist/${file}`);
});

// Copiar arquivos adicionais
console.log('📁 Copiando arquivos adicionais para dist/...');
additionalFiles.forEach(file => {
  copyFile(file, `dist/${file}`);
});

// Copiar pasta public para dist
console.log('📁 Copiando pasta public/ para dist/...');
if (fs.existsSync('public')) {
  const publicFiles = fs.readdirSync('public');
  publicFiles.forEach(file => {
    const sourcePath = path.join('public', file);
    const destPath = path.join('dist', file);
    
    if (fs.statSync(sourcePath).isDirectory()) {
      // Copiar diretório recursivamente
      if (!fs.existsSync(destPath)) {
        fs.mkdirSync(destPath, { recursive: true });
      }
      copyDirectory(sourcePath, destPath);
    } else {
      copyFile(sourcePath, destPath);
    }
  });
}

// Copiar pasta tilesets para dist (necessário para GitHub Pages)
console.log('📁 Copiando pasta tilesets/ para dist/...');
if (fs.existsSync('tilesets')) {
  const tilesetsPath = path.join('dist', 'tilesets');
  if (!fs.existsSync(tilesetsPath)) {
    fs.mkdirSync(tilesetsPath, { recursive: true });
  }
  copyDirectory('tilesets', tilesetsPath);
}

// Copiar tilesets principais para a raiz do dist (para URLs simples)
console.log('📁 Copiando tilesets principais para raiz do dist/...');
const mainTilesets = ['WA_Room_Builder.png', 'tileset_colors_walls.png'];
mainTilesets.forEach(tileset => {
  const source = path.join('tilesets', tileset);
  const dest = path.join('dist', tileset);
  copyFile(source, dest);
});

// Função para copiar diretório recursivamente
function copyDirectory(source, dest) {
  if (!fs.existsSync(dest)) {
    fs.mkdirSync(dest, { recursive: true });
  }
  
  const files = fs.readdirSync(source);
  files.forEach(file => {
    const sourcePath = path.join(source, file);
    const destPath = path.join(dest, file);
    
    if (fs.statSync(sourcePath).isDirectory()) {
      copyDirectory(sourcePath, destPath);
    } else {
      copyFile(sourcePath, destPath);
    }
  });
}

console.log('✅ Processo de cópia concluído!');
