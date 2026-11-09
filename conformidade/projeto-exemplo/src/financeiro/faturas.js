// Emissão de faturas (SPEC-002-financeiro)
export function gerarFatura(cliente, valor, mes, ano) {
  const vencimento = new Date(ano, mes - 1, cliente.diaVencimento);
  return { cliente: cliente.nome, valor, vencimento };
}
