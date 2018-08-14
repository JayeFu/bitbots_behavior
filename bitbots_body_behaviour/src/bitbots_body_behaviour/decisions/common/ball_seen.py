# -*- coding:utf-8 -*-
"""
BallSeen
^^^^^^^^

.. moduleauthor:: Martin Poppinga <1popping@informatik.uni-hamburg.de>

"""
import time

import rospy
from bitbots_body_behaviour.body.actions.search import Search
from bitbots_body_behaviour.body.decisions.common.close_ball import CloseBallPenaltyKick, CloseBallCommon
from bitbots_body_behaviour.body.decisions.team_player.fieldie_search_decision import FieldieSearchDecision
from bitbots_stackmachine.abstract_decision_element import AbstractDecisionElement


class AbstractBallSeen(AbstractDecisionElement):
    """
    Entscheidet ob der Ball gesehen wurde bzw. ob die Informationen zuverlässig genug sind
    Decides if the ball was seen rspectively if the information is  authentic enough.
    """

    def __init__(self, connector, _):
        super(AbstractBallSeen, self).__init__(connector)
        self.max_ball_time = connector.config["Body"]["Common"]["maxBallTime"]

    def perform(self, connector, reevaluate=False):
        if (rospy.get_time() - connector.world_model.ball_last_seen()) < self.max_ball_time:
            return self.has_ball_seen(connector)
        else:
            return self.ball_not_seen(connector)

    def get_reevaluate(self):
        return True

    def has_ball_seen(self, connector):
        raise NotImplementedError

    def ball_not_seen(self, connector):
        raise NotImplementedError


class BallSeenFieldie(AbstractBallSeen):
    def has_ball_seen(self, connector):
        return self.push(CloseBallCommon)

    def ball_not_seen(self, connector):
        return self.push(FieldieSearchDecision)


class BallSeenPenaltyKick(AbstractBallSeen):
    def has_ball_seen(self, connector):
        return self.push(CloseBallPenaltyKick)

    def ball_not_seen(self, connector):
        return self.push(Search)
