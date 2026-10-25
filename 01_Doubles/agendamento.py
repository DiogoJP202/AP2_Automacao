"""Mini-projeto de agendamentos: código real, sem dependência de frameworks."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Agendamento:
    cliente: str
    data: str
    horario: str

class HorarioIndisponivelError(ValueError):
    """Erro quando o horário solicitado não pode ser reservado."""

class ServicoAgendamento:
    """Orquestra reserva e confirmação por meio de dependências injetadas."""
    def __init__(self, repositorio, notificador):
        self.repositorio = repositorio
        self.notificador = notificador

    def agendar(self, cliente: str, data: str, horario: str) -> Agendamento:
        if not cliente.strip():
            raise ValueError("Nome do cliente não pode ficar vazio")
        if not self.repositorio.horario_disponivel(data, horario):
            raise HorarioIndisponivelError("Horário indisponível")
        agendamento = Agendamento(cliente=cliente, data=data, horario=horario)
        self.repositorio.salvar(agendamento)
        self.notificador.enviar_confirmacao(agendamento)
        return agendamento
