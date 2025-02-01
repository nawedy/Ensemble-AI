import * as vscode from 'vscode';
import * as path from 'path';
import * as fs from 'fs';

export function activate(context: vscode.ExtensionContext) {
  context.subscriptions.push(
    vscode.commands.registerCommand('aiAssistant.startChat', () => {
      const panel = vscode.window.createWebviewPanel(
        'aiChat', 
        'AI Coding Assistant', 
        vscode.ViewColumn.One, 
        { enableScripts: true }
      );
      
      const htmlPath = path.join(context.extensionPath, 'src', 'webview.html');
      panel.webview.html = fs.readFileSync(htmlPath, 'utf8');
    })
  );
}