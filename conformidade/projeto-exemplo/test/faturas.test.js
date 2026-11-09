import { test } from 'node:test';
import assert from 'node:assert';
import { cadastrarCliente } from '../src/clientes/cadastro.js';
import { gerarFatura } from '../src/financeiro/faturas.js';
test('fatura vence no dia definido no cadastro', () => {
  const c = cadastrarCliente('Ana', '101');
  assert.equal(gerarFatura(c, 500, 3, 2027).vencimento.getDate(), 10);
});
