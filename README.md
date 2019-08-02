# bitbots_behavior

This is the behavior code of the RoboCup Humanoid League team Hamburg Bit-Bots.
It is divided into a behavior for the head and the body.
Both are programmed using the dynamic_stack_decider package (https://github.com/bit-bots/dynamic_stack_decider).

# Node
## Body
* Package: bitbots_behavior
* Name: body_behavior
* Type: body_behavior.py

### Publisher
* strategy_sender
  * topic: "strategy"
  * type: Strategy
* head_pub
  * topic: "head_mode"
  * type: HeadMode
* pathfinding_pub
  * topic:"move_base_simple/goal"
  * type: PoseStamped

### Subscriber
* About ball
  * topic: "ball_relative"
  * type: BallRelative
  * callback: blackboard.world_model.ball_callback
* About goal
  * topic: "goal_relative"
  * type: GoalRelative
  * callback: blackboard.world_model.goal_callback
* About game state
  * topic: "gamestate"
  * type: GameState
  * callback: blackboard.gamestate.gamestate_callback
* About team data
  * topic: "team_data"
  * type: TeamData
  * callback: blackboard.team_data.team_data_callback
* About pose
  * topic: "amcl_pose"
  * type: PoseWithCovarianceStamped
  * callback: blackboard.world_model.position_callback
* About robot state
  * topic: "robot_state"
  * type: RobotControlState
  * callback: blackboard.blackboard.robot_state_callback

## Head
### Publisher
* position_publisher
  * topic: "/head_motor_goals"
  * type: JointCommand
* visual_compass_record_trigger
  * topic: "/visual_compass_ground_truth_trigger"
  * type: Header

### Subscriber
* About headmode
  * topic: "/head_mode"
  * type: HeadModeMsg
  * callback: blackboard.head_capsule.head_mode_callback
* About ball
  * topic: "/ball_relative"
  * type: BallRelative
  * callback: blackboard.world_model.ball_callback
* About head joints
  * topic: "/joint_states"
  * type: JointState
  * callback: blackboard.head_capsule.joint_state_callback
