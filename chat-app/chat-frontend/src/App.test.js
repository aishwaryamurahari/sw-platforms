// import { render, screen } from '@testing-library/react';
// import App from './App';

// test('renders learn react link', () => {
//   render(<App />);
//   const linkElement = screen.getByText(/learn react/i);
//   expect(linkElement).toBeInTheDocument();
// });

import { render, screen } from '@testing-library/react';
import App from './App';

// Mock ChatRoom component to prevent issues with untested child components
jest.mock('./components/ChatRoom', () => () => <div data-testid="chatroom">Chat Room</div>);

test('renders ChatRoom component', () => {
  render(<App />);
  const chatRoomElement = screen.getByTestId('chatroom');
  expect(chatRoomElement).toBeInTheDocument();
});

