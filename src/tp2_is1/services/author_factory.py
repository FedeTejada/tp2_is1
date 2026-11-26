from tp2_is1.extensions import db
from tp2_is1.models.agent_ai import Agent_AI
from tp2_is1.models.user import User


class AuthorFactory:
    """Factory Method: crea/obtiene Authors sin que Answer conozca la clase concreta."""

    @staticmethod
    def create(kind: str, **kwargs):
        if kind == 'user':
            return User(**kwargs)
        if kind == 'agent':
            return Agent_AI(**kwargs)
        raise ValueError(f"Tipo de autor desconocido: {kind}")

    @staticmethod
    def get_or_create_agent(model: str) -> Agent_AI:
        agent = db.session.scalar(db.select(Agent_AI).where(Agent_AI.model == model))
        if agent is None:
            agent = Agent_AI()
            agent.model = model
            db.session.add(agent)
            db.session.flush()
        return agent
