// Cadastro de condôminos (SPEC-001-clientes)
export const ROTULO_BOTAO_SALVAR = 'Salvar';
export function cadastrarCliente(nome, unidade) {
  if (!nome || !unidade) throw new Error('Nome e unidade são obrigatórios');
  return { nome, unidade, diaVencimento: 10 }; // RN-02: vencimento padrão no dia 10
}
