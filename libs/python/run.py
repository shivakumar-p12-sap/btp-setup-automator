from libs.python.btp_cli import BTPUSECASE

# Run this command in the command line to get all options of this script
# python run.py -h

myBtpUseCase = BTPUSECASE()

#######################################################################################
# Check if the account fits to the usecase_config.json file
#######################################################################################
myBtpUseCase.check_if_account_can_cover_use_case()

#######################################################################################
# Run all commands defined before the account is prepared
#######################################################################################
myBtpUseCase.executeBeforeAccountSetup()

#######################################################################################
# Create the subaccount in the directory if not already existing
#######################################################################################
myBtpUseCase.create_subaccount()

#######################################################################################
# Entitle directory to use defined services and subscriptions for the use case
#######################################################################################
myBtpUseCase.entitle_subaccount()

#######################################################################################
# Create a CF environment in the new subaccount if not already existing
#######################################################################################
myBtpUseCase.initialize_environments()

#######################################################################################
# Create new space if not already existing
#######################################################################################
myBtpUseCase.create_new_cf_space()

#######################################################################################
# Give all colleagues listed as admins in usecase_config.json file all roles within the space
#######################################################################################
myBtpUseCase.assignUsersToSubaccountAndRoles()

#######################################################################################
# Create all app subscriptions and services defined in usecase_config.json file (applications section)
#######################################################################################
myBtpUseCase.create_configured_app_subscriptions_and_services()

#######################################################################################
# Run all commands defined after the account setup is finished
#######################################################################################
myBtpUseCase.executeAfterAccountSetup()

myBtpUseCase.finish()
