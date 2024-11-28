from ipywidgets import Button, Label, HBox, Layout
from IPython.display import display

class TaskCheckbox:
    def __init__(self, task_text):
        # 상태 정의
        self.states = ['미완료', '진행 중', '완료']
        self.state_styles = {
            '미완료': {'button_color': 'white', 'border_color': 'black'},
            '진행 중': {'button_color': '#F6D175', 'border_color': '#F59E4B'},
            '완료': {'button_color': '#388136', 'border_color': '#0E4D22'}
        }
        self.current_state = 0  # 초기 상태 (미완료)
        self.task_text = task_text  # 할 일 텍스트
        
        # 체크박스 모양의 버튼 생성
        self.checkbox = Button(
            description='',
            layout=Layout(width='13px', height='13px', margin='0px 3px 0px 0px', padding='0px'),
            style={'button_color': self.state_styles['미완료']['button_color']}
        )
        
        # 상태를 표시할 레이블 (할 일 텍스트와 상태 표시)
        self.state_label = Label(value=f"{self.task_text} ({self.states[self.current_state]})")
        
        # 초기 스타일 설정
        self.update_checkbox_style()
        
        # 버튼 클릭 이벤트 연결
        self.checkbox.on_click(self.toggle_state)
        
        # HBox로 구성하여 수평 정렬
        self.container = HBox([self.checkbox, self.state_label], layout=Layout(align_items='center'))

    def update_checkbox_style(self):
        # 현재 상태에 맞게 스타일 업데이트
        style = self.state_styles[self.states[self.current_state]]
        self.checkbox.style.button_color = style['button_color']
        self.checkbox.layout.border = f"1px solid {style['border_color']}"
        self.state_label.value = f"{self.task_text} ({self.states[self.current_state]})"

    def toggle_state(self, event):
        # 상태를 순환적으로 변경
        self.current_state = (self.current_state + 1) % len(self.states)
        self.update_checkbox_style()
    
    def display(self):
        # Jupyter Notebook에 표시
        display(self.container)