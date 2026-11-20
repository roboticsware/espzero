from espzero import Stepper

# 1 full rotation per 60 seconds (2048 steps)
STEP_DELAY = 60.0 / 2048

stepper = Stepper((1, 2, 3, 4), step_delay=STEP_DELAY)
stepper.run_continuous(direction="cw")
