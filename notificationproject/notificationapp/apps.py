from django.apps import AppConfig


class NotificationappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notificationapp'



<div class="container">
  <div class="chat-list mat-elevation-z5">
    <div class="search-input">
      <mat-form-field>
        <input
          matInput
          placeholder="Search for users and start a chat"
          [matAutocomplete]="users"
          [formControl]="searchControl"
        />
        <mat-icon>search</mat-icon>
      </mat-form-field>
      
        
     
      <mat-autocomplete #users="matAutocomplete">
        <mat-option>
        </mat-option>
      </mat-autocomplete>
    </div>
    <mat-selection-list [multiple]="false" [formControl]="chatListControl">
      <mat-divider></mat-divider>
      <mat-list-option>
        <img
          matListAvatar
         
        />
        <p mat-line class="chat-title">
          <span class="chat-name">fmklef</span
          ><span class="chat-date">
          
         </span>
        </p>
        <p mat-line>vkjhjlkj</p>
        <mat-divider></mat-divider>
      </mat-list-option>
    </mat-selection-list>
  </div>
  <div class="messages mat-elevation-z5">
    <div
      class="messages-header"
      
    >
      <img
       
      />
      <h2></h2>
    </div>
    <ng-template #noChatSelected>
      <h2>Messages</h2>
    </ng-template>
    <mat-divider></mat-divider>
    <div class="chat-area">
      <ng-container >
        <ng-container >
          <div
            class="chat-bubble-container"
            
          >
            <div class="chat-bubble">
             
              <span class="chat-time">
     </span>
            </div>
          </div>
        </ng-container>
      </ng-container>
      <div #endOfChat></div>
    </div>
    <div class="input-area">
      <mat-form-field appearance="outline">
        <input
          matInput
          placeholder="Enter your message..."
          [formControl]="messageControl"
          (keydown.enter)="sendMessage()"
        />
        <button mat-icon-button matSuffix (click)="sendMessage()">
          <mat-icon>send</mat-icon>
        </button>
      </mat-form-field>
    </div>
  </div>
</div>










.container {
    display: flex;
    height: calc(100vh - 70px);
    margin-top: 8%;

    > .chat-list {
        width: 40%;
        margin: 16px;
        background: #6d716e;
        border-radius: 16px;

        .chat-title {

            display: flex;
            justify-content: space-between;

            .chat-name {  
                font-weight: 500;
            }

            .chat-date {
                font-size: 0.7rem;
                color: rgba(0,0,0,0.7)
            }
            
        }

        .search-input {
            margin: 24px;
        }
    }

    > .messages {
        width: 60%;
        padding: 24px;
        margin: 16px;
        margin-left: 8px;
        border-radius: 16px;
      

        .messages-header {
            display: flex;
            margin-bottom: 8px;

             > img {
                 border-radius: 50%;
                 object-fit: cover;
                 margin-right: 16px;
                 height: 35px;
             }

             > h2 {
                margin: 0;
             }
        }

        .chat-area {
            height: calc(100vh - 270px);
            display: flex;
            flex-direction: column;
            align-items: flex-start;

            overflow: auto;

            > :first-child {
                margin-top: auto;
            }

            .chat-bubble-container {

                display: flex;
                width: 100%;
                justify-content: flex-start;

                > .chat-bubble {
                    background: white;
                    padding-top: 8px;
                    padding-bottom: 18px;
                    padding-left: 8px;
                    padding-right: 100px;
                    margin-bottom: 16px;
                    border-radius: 8px;
                    width: fit-content;

                    position: relative;

                    > .chat-time {
                        position: absolute;
                        bottom: 2px;
                        right: 8px;
                        font-size: 0.7rem;
                        color: rgba(0,0,0,0.6);
                    }
                }
                
            }

            .chat-bubble-container.sender {
                justify-content: flex-end;
                
                > .chat-bubble {
                    background: #c5cae9;
                }
            }

        }

        .input-area {
            padding-top: 16px;
            padding-bottom: 8px;
        }
    }
}

mat-form-field {
    width: 100%;
}