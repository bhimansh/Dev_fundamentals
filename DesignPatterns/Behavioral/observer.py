"""
One object (subject) maintains a list of dependents (observers) and
notifies them automatically of any state changes.

✅ When to Use Observer Pattern
        Situation	                                |       Reason
You have a one-to-many dependency	                | One subject, many observers
When you need automatic updates on state change     | Observers get notified immediately
You want to decouple subject and observers	        | Observers can vary and be added dynamically

Examples:	UI components (MVC), event systems, chat apps, data listeners

❌ When NOT to Use It
        Situation	                                |           Reason
Only one object needs the update	                | Too much complexity for little gain
Tight control over update order is needed	        | Notifications happen in unpredictable order
Observers need a lot of data from subject	        | Might break encapsulation or become inefficient
Circular updates can occur	                        | Hard to debug when observers update the subject again

"""

from abc import ABC, abstractmethod

class BaseObserver(ABC):
    @abstractmethod
    def update(self, msg):
        pass

class EmailObserver(BaseObserver):
    def update(self, message):
        print(f'Received message via Email: {message}')

class SMSObserver(BaseObserver):
    def update(self, message):
        print(f'Received message via SMS: {message}')

# Publisher
class EventManager:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, observer):
        self._subscribers.append(observer)

    def unsubscribe(self, observer):
        self._subscribers.remove(observer)

    def notify(self, event):
        for subscriber in self._subscribers:
            subscriber.update(event)

if __name__ == '__main__':
    event_manager = EventManager()
    event_manager.subscribe(EmailObserver())
    event_manager.subscribe(SMSObserver())
    event_manager.notify('New Update on the topic')
