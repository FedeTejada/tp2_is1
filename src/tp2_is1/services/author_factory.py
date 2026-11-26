from tp2_is1.extensions import db
from tp2_is1.models.agentAI import AgentAI
from tp2_is1.models.user import User


class AuthorFactory:
    """Factory Method: crea/obtiene Authors sin que Answer conozca la clase concreta."""

    @staticmethod
    def create(kind: str, **kwargs):
        if kind == 'user':
            return User(**kwargs)
        if kind == 'agent':
            return AgentAI(**kwargs)
        raise ValueError(f"Tipo de autor desconocido: {kind}")

    @staticmethod
    def get_or_create_agent(model: str) -> AgentAI:
        agent = db.session.scalar(db.select(AgentAI).where(AgentAI.model == model))
        if agent is None:
            agent = AuthorFactory.create('agent', model=model)
            db.session.add(agent)
            db.session.flush()
        return agent
