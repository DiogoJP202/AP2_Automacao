"""Dois doublés de teste: Stub (resposta fixa) e Spy (observação de chamadas)."""

class RepositorioAgendamentosStub:
    """STUB: substitui o banco e retorna disponibilidade definida no teste."""
    def __init__(self, disponivel=True):
        self.disponivel = disponivel
        self.registros = []

    def horario_disponivel(self, data, horario):
        return self.disponivel

    def salvar(self, agendamento):
        self.registros.append(agendamento)

class NotificadorSpy:
    """SPY: substitui o envio de e-mail e registra chamadas."""
    def __init__(self):
        self.confirmacoes = []

    def enviar_confirmacao(self, agendamento):
        self.confirmacoes.append(agendamento)
