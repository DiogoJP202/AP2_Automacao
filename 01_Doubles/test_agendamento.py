"""Testes unitários com dois tipos distintos de doublés."""
import unittest
from agendamento import HorarioIndisponivelError, ServicoAgendamento
from doubles import NotificadorSpy, RepositorioAgendamentosStub

class TestServicoAgendamento(unittest.TestCase):
    def setUp(self):
        self.repositorio = RepositorioAgendamentosStub(disponivel=True)
        self.notificador = NotificadorSpy()
        self.servico = ServicoAgendamento(self.repositorio, self.notificador)

    def test_stub_permite_agendamento_quando_horario_disponivel(self):
        agendamento = self.servico.agendar("Marina", "2026-11-10", "14:00")
        self.assertEqual(agendamento.cliente, "Marina")
        self.assertEqual(self.repositorio.registros, [agendamento])

    def test_stub_bloqueia_agendamento_quando_horario_indisponivel(self):
        self.repositorio.disponivel = False
        with self.assertRaisesRegex(HorarioIndisponivelError, "Horário indisponível"):
            self.servico.agendar("Marina", "2026-11-10", "14:00")
        self.assertEqual(self.repositorio.registros, [])
        self.assertEqual(self.notificador.confirmacoes, [])

    def test_spy_registra_uma_confirmacao_com_dados_corretos(self):
        agendamento = self.servico.agendar("Caio", "2026-11-10", "15:00")
        self.assertEqual(len(self.notificador.confirmacoes), 1)
        self.assertEqual(self.notificador.confirmacoes[0], agendamento)

    def test_nome_vazio_nao_deve_reservar_nem_notificar(self):
        with self.assertRaises(ValueError):
            self.servico.agendar("  ", "2026-11-10", "15:00")
        self.assertEqual(self.repositorio.registros, [])
        self.assertEqual(self.notificador.confirmacoes, [])

if __name__ == "__main__":
    unittest.main(verbosity=2)
