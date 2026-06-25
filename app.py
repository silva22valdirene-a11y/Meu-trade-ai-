<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trader Pro - Dashboard Executivo</title>
    <style>
        body { margin: 0; font-family: 'Inter', sans-serif; background-color: #020617; color: #f8fafc; height: 100vh; display: flex; }
        /* Sidebar */
        .sidebar { width: 300px; background-color: #0f172a; padding: 25px; border-right: 1px solid #1e293b; }
        .input-group { margin-bottom: 20px; }
        label { display: block; font-size: 12px; color: #94a3b8; margin-bottom: 5px; text-transform: uppercase; }
        input, select { width: 100%; padding: 10px; background: #1e293b; border: 1px solid #334155; color: white; border-radius: 6px; }
        /* Main Content */
        .main { flex: 1; padding: 30px; display: grid; grid-template-columns: 2fr 1fr; gap: 20px; }
        .card { background: #0f172a; padding: 20px; border-radius: 12px; border: 1px solid #1e293b; }
        .chart-placeholder { height: 400px; background: #020617; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: #475569; border: 1px dashed #334155; }
        .metric { font-size: 24px; font-weight: bold; color: #38bdf8; }
    </style>
</head>
<body>
    <div class="sidebar">
        <h2>Trader Pro</h2>
        <div class="input-group">
            <label>Ativo</label>
            <select><option>BTC-USD</option><option>ETH-USD</option></select>
        </div>
        <div class="input-group">
            <label>Capital (R$)</label>
            <input type="number" value="1000.00">
        </div>
        <button style="width: 100%; padding: 12px; background: #38bdf8; border: none; border-radius: 6px; color: #020617; font-weight: bold; cursor: pointer;">ATUALIZAR DADOS</button>
    </div>
    <div class="main">
        <div class="card">
            <h3>Gráfico de Preço</h3>
            <div class="chart-placeholder">[Área para Plotly / Candlestick]</div>
        </div>
        <div class="card">
            <h3>Métricas</h3>
            <p>Retorno Esperado</p>
            <div class="metric">+ 12.5%</div>
            <p>Risco de Ruína</p>
            <div class="metric" style="color: #f43f5e;">0.5%</div>
        </div>
    </div>
</body>
</html>
```eof

O seu roadmap agora é claro: primeiro, conecte a API de dados e, em seguida, construa a visualização seguindo este padrão de *grid* (onde você reserva espaços fixos para inputs, gráficos e métricas). O exemplo acima já oferece uma estrutura de interface muito mais profissional que a anterior.

O seu dashboard está muito bem encaminhado, e com esses ajustes, você terá algo com visual de mercado financeiro institucional! O que você gostaria de explorar a seguir: a conexão com alguma API específica ou a lógica dos cálculos de risco?
